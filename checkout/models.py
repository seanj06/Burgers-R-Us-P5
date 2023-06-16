import uuid
from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.conf import settings
from products.models import Food
from profiles.models import Profile

# Delay in minutes to earliest delivery time option
DELIVERY_TIME_DELAY = 90


class Order(models.Model):
    """
    Model for food orders
    """
    # Choices for delivery times
    DELIVERY_TIME_CHOICES = [
        (i, (
            timezone.now() + timezone.timedelta(minutes=i+DELIVERY_TIME_DELAY)
            ).strftime('%H:%M'))
        for i in range(0, 300-DELIVERY_TIME_DELAY, 15)
    ]

    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True,
        blank=True, related_name='orders'
        )    
    full_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=True, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    eircode = models.CharField(max_length=10, null=False, blank=False)
    county = models.CharField(max_length=30, null=False, blank=False)
    town = models.CharField(max_length=20, null=False, blank=False)
    address_1 = models.CharField(max_length=80, null=False, blank=False)
    address_2 = models.CharField(max_length=80, null=True, blank=True)
    address_3 = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_time = models.IntegerField(
        choices=DELIVERY_TIME_CHOICES, null=True
        )
    delivery_cost = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
        )
    order_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
        )
    grand_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, default=0
        )

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def update_total(self):
        """
        Update grand total each time a line item is added,
        accounting for delivery costs.
        """
        self.order_total = self.order_item.aggregate(
            Sum('order_item_total'))['order_item_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = (
                self.order_total * settings.STANDARD_DELIVERY_PERCENTAGE / 100
            )
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number    


class OrderItem(models.Model):
    """
    Model for food item in the order
    """
    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name='order_item'
        )
    food = models.ForeignKey(
        Food, null=False, blank=False, on_delete=models.CASCADE
        )
    quantity = models.IntegerField(null=False, blank=False, default=0)
    order_item_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False
        )

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.order_item_total = self.food.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.food.sku} on order {self.order.order_number}'    
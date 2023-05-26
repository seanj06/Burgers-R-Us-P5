from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.


class OrderItemAdminInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('order_item_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    Admin customisation for Order model
    """
    inlines = (OrderItemAdminInline,)

    readonly_fields = (
        'order_number', 'date', 'delivery_cost',
        'order_total', 'grand_total',
    )

    fields = (
        'order_number', 'full_name', 'email',
        'eircode', 'county', 'town', 'address_1',
        'address_2', 'address_3', 'date', 'delivery_time',
        'delivery_cost', 'order_total', 'grand_total',
    )

    list_display = (
        'order_number', 'date', 'full_name',
        'delivery_time', 'delivery_cost', 'order_total',
        'grand_total',
    )

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)

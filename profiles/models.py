from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Model for user profile
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(
        max_length=20, null=True, blank=True
        )
    default_address_1 = models.CharField(max_length=80)
    default_address_2 = models.CharField(max_length=80, blank=True, null=True)
    default_address_3 = models.CharField(max_length=80, blank=True, null=True)
    default_email = models.EmailField(max_length=254, null=False, blank=False)
    default_eircode = models.CharField(max_length=10, null=True, blank=True)
    default_town = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.userprofile.save()

from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class OTP(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return str(self.otp)

class PremiumUser(models.Model):
    choices = (
        ('1', '1 Month'),
        ('3', '3 Months'),
        ('6', '6 Months'),
        ('12', '12 Months'),
    )
    price_choices = (
        ('1', '100'),
        ('3', '250'),
        ('6', '500'),
        ('12', '1000'),
    )
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    is_premium = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    duration = models.CharField(max_length=2, choices=choices, default='1')
    price = models.CharField(max_length=4, choices=price_choices, default='1')
    
    def __str__(self):
        return str(self.user)

#add a method to the User model to check if the user is premium
User.add_to_class('is_premium', lambda self: PremiumUser.objects.filter(user=self).exists())


from django.contrib.auth.models import AbstractUser
from django.db import models
from realestate_property.base_model import TimeStamp
from .managers import CustomUserManager






# Create your models here.
class CustomUser(AbstractUser):
    ADMIN = "admin"
    AGENT = "agent"
    BUYER = "buyer"
    SELLER = "seller"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (AGENT, "Agent"),
        (BUYER, "Buyer"),
        (SELLER, "Seller"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    is_verified = models.BooleanField(default=False)
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:  # readable representation
        return self.get_full_name() or self.email

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
class BuyerProfile(TimeStamp):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    interest_area = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"BuyerProfile of {self.user.get_full_name() or self.user.email}"

class SellerProfile(TimeStamp):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    national_id = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    approved = models.BooleanField(default=False)  # Admin Approval

    def __str__(self):
        return f"SellerProfile of {self.user.get_full_name() or self.user.email}"
class AgentProfile(TimeStamp):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    assigned_area = models.CharField(max_length=255)
    agency_name = models.CharField(max_length=255, blank=True)

from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager





# Create your models here.
class CustomUser(AbstractUser):
    ADMIN = "admin"
    AGENT = "agent"
    CUSTOMER = "customer"

    ROLE_CHOICES = [
        (ADMIN, "Admin"),
        (AGENT, "Agent"),
        (CUSTOMER, "Customer"),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=CUSTOMER)
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

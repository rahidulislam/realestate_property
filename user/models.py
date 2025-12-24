from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import ValidationError
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

class AgentApplication(TimeStamp):
    class ApplicationStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        APPROVED = "approved", "Approved"
        REJECTED = "rejected", "Rejected"

    approved_user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True, related_name="agent_applications")
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    license_number = models.CharField(max_length=50)
    national_id = models.CharField(max_length=30)
    nid_document = models.FileField(upload_to="agent_applications/nid_documents/")
    license_document = models.FileField(upload_to="agent_applications/license_documents/")
    experience_years = models.PositiveIntegerField()
    company_name = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=ApplicationStatus.choices,
        default=ApplicationStatus.PENDING,
    )

    approved_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"AgentApplication({self.full_name}, {self.email}, {self.status})"
    
            
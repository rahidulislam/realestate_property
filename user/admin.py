from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils import timezone
from django.conf import settings

from .models import (
    AgentApplication,
    AgentProfile,
    BuyerProfile,
    CustomUser,
    SellerProfile,
)


# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
        (("Role"), {"fields": ("role",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "role"),
            },
        ),
    )
    list_display = ("email", "first_name", "last_name", "is_staff", "role")
    list_filter = ("is_staff", "is_superuser", "is_active", "role")
    ordering = ("email",)


admin.site.register(BuyerProfile)
# admin.site.register(SellerProfile)
admin.site.register(AgentProfile)


@admin.register(SellerProfile)
class SellerProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "approved")
    list_filter = ("approved",)
    actions = ["approve_sellers"]

    def approve_sellers(self, request, queryset):
        user_ids = queryset.values_list("user_id", flat=True)
        CustomUser.objects.filter(id__in=user_ids).update(is_active=True)
        queryset.update(approved=True)


@admin.action(description="Approve selected agent applications")
def approve_agent_applications(modeladmin, request, queryset):

    
    for application in queryset:
        first_name = application.full_name.split(" ")[0]
        last_name = " ".join(application.full_name.split(" ")[1:]) or ""
        # skip if already approved
        if application.status == "approved":
            continue

        # Prevent duplicate agent profiles
        user, created = CustomUser.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            email=application.email,
            defaults={
                "role": "agent",
                "is_active": True,
            },
        )
        if created:
            # agent should set password via email
            user.set_unusable_password()
            user.save()

            # Create or get associated AgentProfile
            agent_profile, profile_created = AgentProfile.objects.get_or_create(
                user=user,
                defaults={
                    "phone": application.phone,
                    "agency_name": application.company_name,
                    "assigned_area": "",  # Add default if needed
                },
            )
            print("Profile created:", profile_created)

            if profile_created:
                # Send password setup email for new agents
                reset_form = PasswordResetForm({"email": user.email})
                if reset_form.is_valid():
                    reset_form.save(
                        request=request,
                        use_https=request.is_secure(),
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        email_template_name="user/email/password_reset_email.txt",
                        html_email_template_name="user/email/password_reset_email.html",
                        subject_template_name="user/email/password_reset_subject.txt",
                    )
                print("Sending reset email to:", user.email)
        # update application
        application.status = "approved"
        application.approved_user = user
        application.approved_at = timezone.now()
        application.save()
    messages.success(request, "Selected agent applications have been approved.")


@admin.register(AgentApplication)
class AgentApplicationAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "status", "created_at")
    list_filter = ("status", "created_at")
    actions = [approve_agent_applications]
    readonly_fields = ("status","approved_user", "approved_at", "created_at", "updated_at")

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status == "approved":
            return [field.name for field in self.model._meta.fields]
        return super().get_readonly_fields(request, obj)

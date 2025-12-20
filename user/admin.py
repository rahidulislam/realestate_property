from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import AgentProfile, BuyerProfile, CustomUser, SellerProfile


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

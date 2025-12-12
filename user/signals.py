# accounts/signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.mail import send_mail
from .models import BuyerProfile, SellerProfile, AgentProfile

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    """
    When a User is created:
      - create BuyerProfile for buyer
      - create SellerProfile for seller (approved=False by default)
      - create AgentProfile for agent (admin should create agents usually)
    """
    if not created:
        return

    user = instance

    if user.user_type == 'buyer':
        BuyerProfile.objects.get_or_create(user=user)
        # mark verified by default for buyers (you may change this policy)
        if not user.is_verified:
            user.is_verified = True
            user.save(update_fields=['is_verified'])

    elif user.user_type == 'seller':
        SellerProfile.objects.get_or_create(user=user)
        # keep seller unapproved by default (admin needs to approve)
        # notify admins about new seller request (optional)
        try:
            admin_emails = [a[1] for a in settings.ADMINS]
        except Exception:
            admin_emails = []

        if admin_emails:
            subject = 'New Seller Registration Pending Approval'
            message = f'A new seller registered: {user.get_full_name() or user.username}\n\n' \
                      f'Email: {user.email}\nPlease review and approve in admin panel.'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, admin_emails, fail_silently=True)

    elif user.user_type == 'agent':
        # Agents normally are created by admin; still we create profile if created
        AgentProfile.objects.get_or_create(user=user)
        # consider forcing is_verified True for admin created agents
        if not user.is_verified:
            user.is_verified = True
            user.save(update_fields=['is_verified'])

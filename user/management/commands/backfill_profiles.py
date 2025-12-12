# accounts/management/commands/backfill_profiles.py
from django.core.management.base import BaseCommand
from django.conf import settings
from user.models import CustomUser, BuyerProfile, SellerProfile, AgentProfile

class Command(BaseCommand):
    help = 'Backfill profiles for existing users based on user_type'

    def handle(self, *args, **options):
        users = CustomUser.objects.all()
        created_count = 0
        for u in users:
            if u.role == 'buyer':
                obj, created = BuyerProfile.objects.get_or_create(user=u)
            elif u.role == 'seller':
                obj, created = SellerProfile.objects.get_or_create(user=u)
            elif u.role == 'agent':
                obj, created = AgentProfile.objects.get_or_create(user=u)
            else:
                created = False

            if created:
                created_count += 1

        self.stdout.write(self.style.SUCCESS(f'Profiles created: {created_count}'))

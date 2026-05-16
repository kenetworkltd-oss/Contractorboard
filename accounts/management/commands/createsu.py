from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = 'Creates a superuser automatically'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='kenny').exists():
            User.objects.create_superuser(
                username='kenny',
                email='kenny@flyvark.ai',
                password='Kenny@FlyVark2026',
                user_type='homeowner'
            )
            self.stdout.write('Superuser created successfully!')
        else:
            self.stdout.write('Superuser already exists.')
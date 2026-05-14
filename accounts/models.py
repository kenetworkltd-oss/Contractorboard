from django.contrib.auth.models import AbstractUser
from django.db import models


NICHE_CHOICES = [
    ('HVAC', 'HVAC'),
    ('Plumbing', 'Plumbing'),
    ('Roofing', 'Roofing'),
    ('Electrical', 'Electrical'),
]


class User(AbstractUser):
    CONTRACTOR = 'contractor'
    HOMEOWNER = 'homeowner'

    USER_TYPE_CHOICES = [
        (CONTRACTOR, 'Contractor'),
        (HOMEOWNER, 'Homeowner'),
    ]

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=HOMEOWNER
    )

    def is_contractor(self):
        return self.user_type == self.CONTRACTOR

    def is_homeowner(self):
        return self.user_type == self.HOMEOWNER


class ContractorProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='contractor_profile'
    )
    business_name = models.CharField(max_length=100)
    niche = models.CharField(max_length=20, choices=NICHE_CHOICES)
    service_area = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to='profiles/', blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.business_name
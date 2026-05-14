from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings

NICHE_CHOICES = [
    ('HVAC', 'HVAC'),
    ('Plumbing', 'Plumbing'),
    ('Roofing', 'Roofing'),
    ('Electrical', 'Electrical'),
]

STATUS_CHOICES = [
    ('open', 'Open'),
    ('filled', 'Filled'),
    ('closed', 'Closed'),
]

class Job(models.Model):
    homeowner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='jobs'
    )
    title = models.CharField(max_length=150)
    description = models.TextField()
    niche = models.CharField(max_length=20, choices=NICHE_CHOICES)
    location = models.CharField(max_length=100)
    budget_min = models.DecimalField(max_digits=8, decimal_places=2)
    budget_max = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} — {self.location}"
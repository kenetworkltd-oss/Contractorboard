from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings
from jobs.models import Job


class Inquiry(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('responded', 'Responded'),
        ('hired', 'Hired'),
        ('closed', 'Closed'),
    ]

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name='inquiries'
    )
    contractor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='sent_inquiries'
    )
    message = models.TextField()
    status = models.CharField(
        max_length=15,
        choices=STATUS_CHOICES,
        default='new'
    )
    sent_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['job', 'contractor']
        ordering = ['-sent_at']

    def __str__(self):
        return f"Inquiry from {self.contractor.username} on {self.job.title}"


class Review(models.Model):
    contractor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews_received'
    )
    homeowner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reviews_given'
    )
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['contractor', 'homeowner']

    def __str__(self):
        return f"{self.rating}★ for {self.contractor.username}"
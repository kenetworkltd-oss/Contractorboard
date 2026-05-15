from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, ContractorProfile

NICHE_CHOICES = [
    ('HVAC', 'HVAC'),
    ('Plumbing', 'Plumbing'),
    ('Roofing', 'Roofing'),
    ('Electrical', 'Electrical'),
]

class ContractorRegistrationForm(UserCreationForm):
    business_name = forms.CharField(max_length=100)
    niche = forms.ChoiceField(choices=NICHE_CHOICES)
    service_area = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class HomeownerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
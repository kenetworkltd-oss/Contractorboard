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
    business_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    niche = forms.ChoiceField(
        choices=NICHE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    service_area = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class HomeownerRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
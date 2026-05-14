from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description', 'niche', 'location', 'budget_min', 'budget_max']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
            'title': forms.TextInput(attrs={'placeholder': 'e.g. Fix AC unit in 3 bedroom house'}),
            'location': forms.TextInput(attrs={'placeholder': 'e.g. Los Angeles, CA'}),
        }
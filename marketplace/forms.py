from django import forms
from .models import Inquiry, Review


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 5,
                'placeholder': 'Describe your experience, availability and estimated cost...',
                'class': 'form-control'
            })
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 4,
                'class': 'form-control'
            }),
            'rating': forms.Select(attrs={'class': 'form-control'})
        }
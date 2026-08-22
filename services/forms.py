from django import forms
from .models import ServiceFeedback, GrantApplication


class ServiceFeedbackForm(forms.ModelForm):
    class Meta:
        model = ServiceFeedback
        fields = ['email', 'text']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Email (необов\'язково)'}),
            'text': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Ваш відгук'}),
        }


class GrantApplicationForm(forms.ModelForm):
    class Meta:
        model = GrantApplication
        fields = ['team_name', 'email', 'city', 'latitude', 'longitude', 'text']
        widgets = {
            'team_name': forms.TextInput(attrs={'placeholder': 'Назва команди або ім\'я'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email'}),
            'city': forms.TextInput(attrs={'placeholder': 'Місто'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'text': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Текст заявки'}),
        }

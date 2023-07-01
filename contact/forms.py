from django import forms
from .models import ContactMessage


class ContactMessageForm(forms.ModelForm):
    """
    Form for ContactMessage Model
    """
    class Meta:
        model = ContactMessage
        fields = ['issue', 'name', 'email', 'subject', 'message']
        widgets = {
            'issue': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }

from django import forms
from django.contrib.auth.models import User

class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    
    



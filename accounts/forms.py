from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class SignupForm(UserCreationForm):
    email=forms.CharField(max_length=100,validators=[validate_email])
    def clean_email(self):
        email=self.cleaned_data['email']
        if email.find('@yahoo')!=-1:
            raise ValidationError("Yahoo Not Allowed",)
        return email
    
    class Meta:
        model=User
        fields=['username','email','password1','password2']


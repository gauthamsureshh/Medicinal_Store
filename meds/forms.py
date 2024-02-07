from django import forms
from .models import Medicine

class MedForm(forms.ModelForm):
    class Meta:
        model=Medicine
        fields='__all__'
        
class SearchForm(forms.Form):
    query=forms.CharField(max_length=50)
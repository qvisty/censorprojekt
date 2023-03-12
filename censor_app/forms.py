# censor_app/forms.py

from django import forms
from .models import Skole

class SkoleForm(forms.ModelForm):
    class Meta:
        model = Skole
        fields = ['navn', 'adresse']

# censor_app/forms.py

from django import forms
from .models import Skole, Lærer, Eksamen, Censor, Skoleklasse


class SkoleForm(forms.ModelForm):
    class Meta:
        model = Skole
        fields = "__all__"


class LærerForm(forms.ModelForm):
    class Meta:
        model = Lærer
        fields = "__all__"


class EksamenForm(forms.ModelForm):
    class Meta:
        model = Eksamen
        fields = "__all__"


class CensorForm(forms.ModelForm):
    class Meta:
        model = Censor
        fields = "__all__"


class SkoleklasseForm(forms.ModelForm):
    class Meta:
        model = Skoleklasse
        fields = "__all__"

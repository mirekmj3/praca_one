from django.forms import ModelForm
from .models import SWATH
from django import forms

class SWATHform(ModelForm):
    class Meta:
        model = SWATH
        fields ='__all__'


class SWATHform2(forms.Form):
    class meta:
        model = SWATH
        fields ='__all__'


class SWATHform3 (forms.Form):
    poczatek = forms.CharField()
    koniec = forms.CharField()
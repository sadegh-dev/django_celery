from django import forms
from .models import SumNumbers

class SumNumbersForm(forms.ModelForm):
    class Meta :
        model= SumNumbers
        fields = ('q','w')

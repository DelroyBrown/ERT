from django import forms
from .models import AmountMade


class AmountMadeForm(forms.ModelForm):
    class Meta:
        model = AmountMade
        fields = ['amount_made']

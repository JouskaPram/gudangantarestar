from django.forms import ModelForm
from django import forms
from scanantares.models import *


class FormSortir(ModelForm):
    class Meta:
        model = Sortir
        fields = '__all__'

        widgets = {
            'barcode': forms.TextInput(),
            'scanner_id': forms.Select(),
        }



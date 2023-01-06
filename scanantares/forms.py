from django.forms import ModelForm
from django import forms
from scanantares.models import *




class FormSortir(ModelForm):
    class Meta:
        model = Sortir
        fields = '__all__'

        widgets = {
            'barcode': forms.TextInput({'class' : 'py-3 px-4  w-full border-gray-200 shadow-sm rounded-l-md text-sm focus:z-10 focus:border-blue-500 focus:ring-blue-500 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400',}),
            'scanner_id': forms.RadioSelect({'class' : 'mt-2  justify-between radio'}),
        }



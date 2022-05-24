from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth import authenticate
from ibmn.breaking.models import Breaking

class CreateBreakForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text','data-constraints':'@Required'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'id':'formFile','type':'file', 'class':'control'}))

   
   
   
    class Meta:
            model = Breaking
            fields = [ "text",
                       "image",
                    ]

    
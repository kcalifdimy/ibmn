from unittest.util import _MAX_LENGTH
from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth import authenticate
from ibmn.bignews.models import Bignews
from ibmn.categories.models import Category

from mptt.forms import TreeNodeChoiceField 
from ckeditor_uploader.widgets import  CKEditorUploadingWidget


class CreateBignewsForm(forms.ModelForm):



    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text',  'data-constraints':'@Required'}))
    short_txt = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text','data-constraints':'@Required'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'id':'formFile','type':'file', 'class':'control'}))
    slug = forms.SlugField(widget=forms.TextInput(attrs={"class": "form-control", 'type':'text'}))
   # pub_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    category_name = forms.ModelChoiceField(queryset=Category.objects.all())
    body_txt =forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control', 'rows':'5', 'cols':'50','data-constraints':'@Required'}))
   
   
   
   
    class Meta:
            model = Bignews
            fields = [
                    "title",
                    "short_txt",
                    "body_txt",
                    "slug",
                   # "pub_date",
                    "image",
                    "category_name",
                    ]

    
   
    
          

class EditBigNewsForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text',  'data-constraints':'@Required'}))
    short_txt = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text','data-constraints':'@Required'}))
    #timestamp = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'id':'formFile','type':'file', 'class':'control'}))
    slug = forms.SlugField(widget=forms.TextInput(attrs={"class": "form-control", 'type':'text'}))
    #pub_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    category_name = forms.ModelChoiceField(queryset=Category.objects.all())
    body_txt =forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control', 'rows':'5', 'cols':'50','data-constraints':'@Required'}))
    
    
   
   
    class Meta:
            model = Bignews
            fields = [
                    "title",
                    "short_txt",
                    "slug",
                    #"pub_date",
                    "image",
                    "category_name",
                    "body_txt",
                    "tags"
                    ]


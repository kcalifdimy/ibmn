from django import forms
from django.forms import ModelChoiceField
from django.contrib.auth import authenticate
from ibmn.news.models import News
from ibmn.categories.models import Subcategory
from mptt.forms import TreeNodeChoiceField , TreeNodeMultipleChoiceField
from ckeditor_uploader.widgets import  CKEditorUploadingWidget


class CreateNewsForm(forms.ModelForm):



    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text',  'data-constraints':'@Required'}))
    short_txt = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text','maxlength':'200','minlength':'60','data-constraints':'@Required'}))
    #timestamp = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'id':'formFile','type':'file', 'class':'control'}))
    slug = forms.SlugField(widget=forms.TextInput(attrs={"class": "form-control", 'type':'text'}))
    #pub_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    body_txt =forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control', 'rows':'5', 'cols':'50','data-constraints':'@Required'}))
   
   
   
   
    class Meta:
            model = News
            fields = [
                    "title",
                    "short_txt",
                    "body_txt",
                    "slug",
                    #"pub_date",
                    "image",
                    "category",
                    ]

  
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'] = TreeNodeChoiceField(queryset=Subcategory.objects.all(),  level_indicator='+--')

           

    def clean_image(self):

        IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

        uploaded_image = self.cleaned_data.get("image",  False)

        extension = str(uploaded_image).split('.')[-1]

        file_type = extension.lower()

        if not uploaded_image:       
            raise forms.ValidationError("please upload an Image") # handle empty image


        if file_type not in IMAGE_FILE_TYPES:
            raise forms.ValidationError("File is not image.")

        return uploaded_image


    

class EditNewsForm(forms.ModelForm):

    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text',  'data-constraints':'@Required'}))
    short_txt = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text','data-constraints':'@Required'}))
    #timestamp = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'id':'formFile','type':'file', 'class':'control'}))
    slug = forms.SlugField(widget=forms.TextInput(attrs={"class": "form-control", 'type':'text'}))
    pub_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}))
    category_name = forms.ChoiceField(label='', widget=forms.Select(attrs={'class':'form-select', 'aria-label':'Default select example'}))
    body_txt =forms.CharField(widget=CKEditorUploadingWidget(attrs={'class':'form-control', 'rows':'5', 'cols':'50','data-constraints':'@Required'}))
    
    
   
   
    class Meta:
            model = News
            fields = [
                    "title",
                    "short_txt",
                    "slug",
                    "pub_date",
                    "image",
                    "category_name",
                    "body_txt",
                    ]


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_name'] = TreeNodeChoiceField(queryset=Subcategory.objects.all())


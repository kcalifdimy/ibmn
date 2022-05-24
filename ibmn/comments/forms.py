import email
from django import forms
from ibmn.comments.models import Comment
from mptt.forms import TreeNodeChoiceField


class CommentForm(forms.ModelForm):


    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'text',  'data-constraints':'@Required'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'type':'email',  'data-constraints':'@Required'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control', 'col':'40', 'row':'10', 'data-constraints':'@Required'}))



    class Meta:
        model = Comment
        fields = ('name',  'email', 'content')


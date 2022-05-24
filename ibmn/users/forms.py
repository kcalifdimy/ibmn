from django import forms
from django.contrib.auth import authenticate
from ibmn.users.models import User

class UserLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'name':'username', 'id':'yourUsername', 'type':'text','data-constraints':'@Required'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','name':'password','id':'yourPassword','type':'password','data-constraints':'@Required'}))




    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            user = authenticate(email=email, password=password)
            if not user:
                raise forms.ValidationError("Account Does Not Exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not user.is_active:
                raise forms.ValidationError("Account is not Active.")

        return super(UserLoginForm, self).clean(*args, **kwargs)


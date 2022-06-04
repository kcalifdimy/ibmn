from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.views.generic.base import TemplateView
from django.shortcuts import render, redirect, reverse
from ibmn.users.forms import UserLoginForm
from django.contrib.auth.mixins import LoginRequiredMixin



class LoginView(View):
    template_name = 'manager_pages/login.html'
    form_class = UserLoginForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)  
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('news:manager_home')
        message = 'Login failed!'
        return render(request, self.template_name, context={'form': form, 'message': message})




class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')


logout_view  = LogoutView.as_view() 
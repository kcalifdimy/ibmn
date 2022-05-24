from django.shortcuts import render

# Create your views here.
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , DetailView, UpdateView, TemplateView, DeleteView
from ibmn.breaking.models import Breaking
from ibmn.breaking.forms import CreateBreakForm
from django import forms


# Create your views here.

class BreakCreateView(View):
    template_name = 'manager_pages/break_add_news.html'
    form_class = CreateBreakForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})


    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request,self.template_name, {'form':form})

break_create_view  =  BreakCreateView.as_view()




class BreakListPostView(LoginRequiredMixin, ListView):
    model = Breaking
    context_object_name = 'break_list'
    template_name = 'manager_pages/break_list_news.html'

break_list_view  =  BreakListPostView.as_view()



class BreakUpdateView(LoginRequiredMixin, UpdateView):
    # specify the model you want to use
    model = Breaking
    template_name = 'manager_pages/break_update_news.html'

    # specify the fields
    fields = ["text", "image"]

    def get_object(self, queryset=None):
        return Breaking.objects.get(id=self.kwargs.get("uuid"))
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    def get_success_url(self):
       return reverse("news:manager_home")
   

break_update_view  = BreakUpdateView.as_view()




class BreakingManagerDeleteView(LoginRequiredMixin, DeleteView):
    # specify the model you want to use
    model = Breaking
    template_name = 'manager_pages/break_delete_news.html'

    # specify the fields
    #fields = ["title","short_txt","slug","pub_date","image","body_txt"]

    def get_object(self, queryset=None):
        return Breaking.objects.get(id=self.kwargs.get("uuid"))
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    def get_success_url(self):
       return reverse("news:manager_home")
   

breaking_manager_delete_view = BreakingManagerDeleteView.as_view()



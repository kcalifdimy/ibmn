import email
from unicodedata import category
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , DetailView, UpdateView, TemplateView, DeleteView
from ibmn.news.models import News, news
from ibmn.news.forms import CreateNewsForm, EditNewsForm
from django import forms



# Create your views here.

class NewsCreateView(View):
    template_name = 'manager_pages/add_news.html'
    form_class = CreateNewsForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})


    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return render(request,self.template_name, {'form':form})

news_create_view   = NewsCreateView.as_view()

class NewsDetailView(DetailView):
    model = News
    template_name = 'pages/news_detail.html'

news_detail_view   = NewsDetailView.as_view()




class ManagerHomeView(LoginRequiredMixin, TemplateView):
    template_name = 'manager_pages/home.html'       

manager_home_view  = ManagerHomeView.as_view()



class ManagerListPostView(LoginRequiredMixin, ListView):
    model = News
    context_object_name = 'news_list'
    template_name = 'manager_pages/news_list.html'


    def get_queryset(self):
        user = self.request.user
        return News.objects.filter(author=user)


manager_list_post_view  = ManagerListPostView.as_view()


class ManagerUpdateView(LoginRequiredMixin, UpdateView):
    # specify the model you want to use
    form_class = EditNewsForm
    model = News
    template_name = 'manager_pages/edit_news.html'

    # specify the fields
    #fields = ["title","short_txt","slug","pub_date","image","body_txt"]

    def get_object(self, queryset=None):
        return News.objects.get(id=self.kwargs.get("uuid"))
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    def get_success_url(self):
       return reverse("news:manager_home")
   

manager_update_view  = ManagerUpdateView.as_view()



class ManagerDeleteView(LoginRequiredMixin, DeleteView):
    # specify the model you want to use
    model = News
    template_name = 'manager_pages/delete_news.html'

    # specify the fields
    #fields = ["title","short_txt","slug","pub_date","image","body_txt"]

    def get_object(self, queryset=None):
        return News.objects.get(id=self.kwargs.get("uuid"))
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    def get_success_url(self):
       return reverse("news:manager_home")
   

manager_delete_view  = ManagerDeleteView.as_view()


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('users:login')


logout_view  = LogoutView.as_view()

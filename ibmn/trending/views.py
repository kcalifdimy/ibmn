from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , DetailView, UpdateView, TemplateView, DeleteView
from ibmn.trending.models import Trending
from ibmn.trending.forms import CreateTrendForm,  EditTrendForm
from django import forms
from ibmn.comments.forms import CommentForm
from ibmn.comments.models import Comment


# Create your views here.

class TrendCreateView(View):
    template_name = 'manager_pages/trending_add_news.html'
    form_class = CreateTrendForm
    
    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})


    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = self.form_class()
            messages.success(request, 'Your news was successfully posted!')

        return render(request,self.template_name, {'form':form})


class TrendListPostView(LoginRequiredMixin, ListView):
    model = Trending
    context_object_name = 'trend_list'
    template_name = 'manager_pages/trending_list_news.html'

trend_list_view  =  TrendListPostView.as_view()



class TrendUpdateView(UpdateView):
    # specify the model you want to use
    form_class =  EditTrendForm
    model = Trending
    template_name = 'manager_pages/trend_update.html'

    # specify the fields
    #fields = ["title","short_txt","slug","pub_date","image","body_txt"]

    def get_object(self, queryset=None):
        return Trending.objects.get(id=self.kwargs.get("uuid"))
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    def get_success_url(self):
       return reverse("trending:trend_list_post")
   

trend_update_view  = TrendUpdateView.as_view()


class TrendManagerDeleteView(LoginRequiredMixin, DeleteView):
    # specify the model you want to use
    model = Trending
    template_name = 'manager_pages/trend_delete_news.html'

    # specify the fields
    #fields = ["title","short_txt","slug","pub_date","image","body_txt"]

    def get_object(self, queryset=None):
        return Trending.objects.get(id=self.kwargs.get("uuid"))
  
    # can specify success url
    # url to redirect after successfully
    # updating details
    def get_success_url(self):
       return reverse("trending:trend_list_post")
   
trend_manager_delete_view = TrendManagerDeleteView.as_view()




def trending_news_details_view(request, slug):
    trendnews = get_object_or_404(Trending, slug=slug)


    similar_trendnews =  trendnews.tags.similar_objects()[:4]




    # List of active comments for this post
    trendnews_comments = trendnews.trendnews_comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.trendnews = trendnews
            # Save the comment to the database
            new_comment.save()
            return redirect(trendnews.get_absolute_url()+'#')
    else:
        comment_form = CommentForm()

    # List of similar posts
    
    return render(request, 'pages/trendnews_details.html', {'trendnews':trendnews,'trendnews_comments': trendnews_comments,
                                                            'comment_form':comment_form, 'similar_trendnews':similar_trendnews
                                                            })


def trending_news_reply_page(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            trendnews_id = request.POST.get('trendnews_id')  # from hidden input
            parent_id = request.POST.get('parent')  # from hidden input
            trendnews_url = request.POST.get('trendnews_url')  # from hidden input
            reply = form.save(commit=False)
    
            reply.post = Trending(id=trendnews_id)
            reply.parent = Comment(id=parent_id)
            reply.save()
            return redirect(trendnews_url+'#')
    return redirect("/")

from unicodedata import category
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , DetailView, UpdateView, TemplateView, DeleteView
from ibmn.categories.models.categories import Category
from ibmn.news.models import News
from ibmn.categories.models import Subcategory
from ibmn.breaking.models import Breaking
from ibmn.comments.forms import CommentForm
from ibmn.comments.models import Comment
from ibmn.trending.models import Trending






def home_view(request):

    breakings = Breaking.objects.all()[:5]

    trend_business_news = Trending.objects.filter(category_name__name='BUSINESS')   
    trend_politics_news = Trending.objects.filter(category_name__name='POLITICS')
    trend_sports_news = Trending.objects.filter(category_name__name='SPORTS')
    trend_arts_news = Trending.objects.filter(category_name__name='ARTS')
    trend_scitech_news = Trending.objects.filter(category_name__name='SCITECH')
    trend_health_news = Trending.objects.filter(category_name__name='HEALTH')
    trend_lifestyle_news = Trending.objects.filter(category_name__name='LIFESTYLE')

    business_news = Subcategory.objects.filter(parent__name='BUSINESS')   
    politics_news = Subcategory.objects.filter(parent__name='POLITICS')
    sports_news = Subcategory.objects.filter(parent__name='SPORTS')
    fashion_news = Subcategory.objects.filter(parent__name='FASHION')
    arts_news = Subcategory.objects.filter(parent__name='ARTS')
    scitech_news = Subcategory.objects.filter(parent__name='SCITECH')
    health_news = Subcategory.objects.filter(parent__name='HEALTH')
    lifestyle_news = Subcategory.objects.filter(parent__name='LIFESTYLE')




       
    context = {


                'trend_business_news':trend_business_news.first(),
                'trend_politics_news':trend_politics_news.first(), 'trend_sports_news':trend_sports_news.first(),
                'trend_arts_news': trend_arts_news.first(), 'trend_scitech_news':trend_scitech_news.first(),
                'trend_health_news':trend_health_news.first(), 'trend_lifestyle_news':trend_lifestyle_news.first(),
                'politics_news': politics_news, 'business_news' : business_news, 'sports_news':sports_news,
                'fashion_news': fashion_news, 'arts': arts_news, 'scitech_news':scitech_news, 'health_news':health_news,
                'lifestyle_news': lifestyle_news ,  'breakings':breakings 
              }

    return render(request, 'pages/home.html', context)





def news_details_view(request, slug):
    news=get_object_or_404(News,slug=slug)

    # List of active comments for this post
    comments = news.comments.filter(active=True)
    new_comment = None
    print('come')
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.news = news
            # Save the comment to the database
            new_comment.save()
            return redirect(news.get_absolute_url()+'#')
    else:
        comment_form = CommentForm()

    # List of similar posts
    
    return render(request, 'pages/news_details.html', {'news':news,'comments': comments,'comment_form':comment_form })


def reply_page(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            news_id = request.POST.get('news_id')  # from hidden input
            parent_id = request.POST.get('parent')  # from hidden input
            news_url = request.POST.get('news_url')  # from hidden input
            reply = form.save(commit=False)
    
            reply.post = News(id=news_id)
            reply.parent = Comment(id=parent_id)
            reply.save()
            return redirect(news_url+'#')
    return redirect("/")
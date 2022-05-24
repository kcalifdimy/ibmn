from multiprocessing import context
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.utils import timezone
from django.views import View
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView , DetailView, UpdateView, TemplateView, DeleteView
from ibmn.news.models import News
from ibmn.categories.models import Category, Subcategory
from ibmn.breaking.models import Breaking
from ibmn.bignews.models import Bignews




def news_cat_view(request):

    big_news = Bignews.objects.filter(category__name='NEWS')
    #popular_news = News.objects.order_by("hit_count_generic__hits")

    global_sub = Subcategory.objects.filter(Q(name='NEWS_GLOBAL_SUB') & Q(parent__name='NEWS'))
    africa_sub = Subcategory.objects.filter(Q(name='NEWS_AFRICA_SUB') & Q(parent__name='NEWS'))
    opinions_sub = Subcategory.objects.filter(Q(name='NEWS_OPINIONS_SUB') & Q(parent__name='NEWS'))
    community_sub = Subcategory.objects.filter(Q(name='NEWS_COMMUNITY_SUB') & Q(parent__name='NEWS'))
   
            
    context = {
            'global_sub':global_sub, 'africa_sub':africa_sub,
            'big_news':big_news.first(),
            'opinions_sub':opinions_sub, 'community_sub':community_sub
            }
    return render(request, 'categories/news_category.html', context)



def politics_cat_view(request):

    big_news = Bignews.objects.filter(category__name='POLITICS')
    #popular_news = News.objects.order_by('-hit_count_generic__hits')[:4]
    global_sub = Subcategory.objects.filter(Q(name='POLITICS_GLOBAL_SUB') & Q(parent__name='POLITICS'))
    africa_sub = Subcategory.objects.filter(Q(name='POLITICS_AFRICA_SUB') & Q(parent__name='POLITICS'))
    community_sub = Subcategory.objects.filter(Q(name='POLITICS_COMMUNITY_SUB') & Q(parent__name='POLITICS'))
    opinions_sub = Subcategory.objects.filter(Q(name='POLITICS_OPINIONS_SUB') & Q(parent__name='POLITICS'))

            
    context = {
            'global_sub':global_sub, 'africa_sub':africa_sub,
            'big_news':big_news.first(),
            'opinions_sub':opinions_sub, 'community_sub':community_sub
            }
    return render(request, 'categories/politics_category.html', context)


def business_cat_view(request):

    big_news = Bignews.objects.filter(category__name='BUSINESS')
    #popular_news = News.objects.order_by('-hit_count_generic__hits')[:4]
    global_sub = Subcategory.objects.filter(Q(name='BUSINESS_GLOBAL_SUB') & Q(parent__name='BUSINESS'))
    igbo_sub = Subcategory.objects.filter(Q(name='BUSINESS_IGBO_SUB') & Q(parent__name='BUSINESS'))
    local_sub = Subcategory.objects.filter(Q(name='BUSINESS_LOCAL_SUB') & Q(parent__name='BUSINESS'))
   
            
    context = {'global_sub':global_sub, 'local_sub':local_sub, 'igbo_sub':igbo_sub,
               'big_news':big_news.first(),
            }
    return render(request, 'categories/business_category.html', context)
   


def sports_cat_view(request):

    big_news = Bignews.objects.filter(category__name='SPORTS')
    #popular_news = News.objects.order_by('-hit_count_generic__hits')[:4]
    global_sub = Subcategory.objects.filter(Q(name='SPORTS_GLOBAL_SUB') & Q(parent__name='SPORTS'))
    local_sub = Subcategory.objects.filter(Q(name='SPORTS_LOCAL_SUB') & Q(parent__name='SPORTS'))
    community_sub = Subcategory.objects.filter(Q(name='SPORTS_COMMUNITY_SUB') & Q(parent__name='SPORTS'))
   
            
    context = {'global_sub':global_sub, 'local_sub':local_sub, 'community_sub':community_sub,
                'big_news':big_news.first(),
                }
    return render(request, 'categories/sports_category.html', context)

def arts_cat_view(request):
    
    big_news = Bignews.objects.filter(category__name='ARTS')
    #popular_news = News.objects.order_by('-hit_count_generic__hits')[:4]

    books_sub = Subcategory.objects.filter(Q(name='ARTS_BOOKS_SUB') & Q(parent__name='ARTS'))
    movies_sub = Subcategory.objects.filter(Q(name='ARTS_MOVIES_SUB') & Q(parent__name='ARTS'))
    music_sub = Subcategory.objects.filter(Q(name='ARTS_MUSIC_SUB') & Q(parent__name='ARTS'))
    showbiz_sub = Subcategory.objects.filter(Q(name='ARTS_SHOWBIZ_SUB') & Q(parent__name='ARTS'))
    event_sub = Subcategory.objects.filter(Q(name='ARTS_EVENT_SUB') & Q(parent__name='ARTS'))
   
            
    context = {
            'books_sub':books_sub, 'movies_sub':movies_sub, 'music_sub':music_sub,
            'big_news':big_news.first(), 
            'showbiz_sub':showbiz_sub, 'event_sub':event_sub
            }
    return render(request, 'categories/arts_category.html', context)

def lifestyle_cat_view(request):

    big_news = Bignews.objects.filter(category__name='LIFESTYLE')
    #popular_news = News.objects.order_by('-hit_count_generic__hits')[:4]

    food_sub = Subcategory.objects.filter(Q(name='LIFESTYLE_FOOD_SUB') & Q(parent__name='LIFESTYLE'))
    culture_sub = Subcategory.objects.filter(Q(name='LIFESTYLE_CULTURE_SUB') & Q(parent__name='LIFESTYLE'))
    fashion_sub = Subcategory.objects.filter(Q(name='LIFESTYLE_FASHION_SUB') & Q(parent__name='LIFESTYLE'))
    travel_sub = Subcategory.objects.filter(Q(name='LIFESTYLE_TRAVEL_SUB') & Q(parent__name='LIFESTYLE'))
    opinions_sub = Subcategory.objects.filter(Q(name='LIFESTYLE_OPINIONS_SUB') & Q(parent__name='LIFESTYLE'))

   
            
    args = {
            'food_sub':food_sub, 'culture_sub':culture_sub,'travel_sub':travel_sub,
            'big_news':big_news.first(),
            'opinions_sub':opinions_sub, 'fashion_sub':fashion_sub
            }
    return render(request, 'categories/lifestyle_category.html', args)

def scitech_cat_view(request):
    

    big_news = Bignews.objects.filter(category__name='SCITECH')
    #popular_news = News.objects.order_by("hit_count_generic__hits")[:4]
    global_sub = Subcategory.objects.filter(Q(name='SCITECH_GLOBAL_SUB') & Q(parent__name='SCITECH'))
    digfintech_sub = Subcategory.objects.filter(Q(name='SCITECH_DIGFIN_SUB') & Q(parent__name='SCITECH'))
    blockchain_sub = Subcategory.objects.filter(Q(name='SCITECH_BLOCKCHAIN_SUB') & Q(parent__name='SCITECH'))
    crypto_sub = Subcategory.objects.filter(Q(name='SCITECH_CRYPTO_SUB') & Q(parent__name='SCITECH'))
    ntf_sub = Subcategory.objects.filter(Q(name='SCITECH_NTF_SUB') & Q(parent__name='SCITECH'))
    web3_sub = Subcategory.objects.filter(Q(name='SCITECH_WEB3_SUB') & Q(parent__name='SCITECH'))
    community_sub = Subcategory.objects.filter(Q(name='SCITECH_COMMUNITY_SUB') & Q(parent__name='SCITECH'))
   
   
   
            
    context = {
            'global_sub':global_sub, 'digitech_fintech_sub':digfintech_sub,
            'big_news':big_news.first(), 
             'web3_sub':web3_sub, 'ntf_sub':ntf_sub,'blockchain_sub':blockchain_sub, 
            ' crypto_sub': crypto_sub, 'community_sub': community_sub
            }
    return render(request, 'categories/scitech_category.html', context)

def health_cat_view(request):

    big_news = Bignews.objects.filter(category__name='HEALTH')
    #popular_news = News.objects.order_by('-hit_count_generic__hits')[:4]
    global_sub = Subcategory.objects.filter(Q(name='HEALTH_GLOBAL_SUB') & Q(parent__name='HEALTH'))
    local_sub = Subcategory.objects.filter(Q(name='HEALTH_LOCAL_SUB') & Q(parent__name='HEALTH'))
    opinions_sub = Subcategory.objects.filter(Q(name='HEALTH_OPINIONS_SUB') & Q(parent__name='HEALTH'))
    community_sub = Subcategory.objects.filter(Q(name='HEALTH_COMMUNITY_SUB') & Q(parent__name='HEALTH'))
   
            
    context = {'global_sub':global_sub, 'local_sub':local_sub, 
                'big_news':big_news.first(), 
                'opinions_sub':opinions_sub, 'community_sub':community_sub}
    return render(request, 'categories/health_category.html', context)


    

    
                    
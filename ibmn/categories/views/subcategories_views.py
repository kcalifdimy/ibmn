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
from ibmn.categories.models import Subcategory
from ibmn.breaking.models import Breaking


# news sub categories
def global_sub_news_cat_view(request):
    
    global_sub = Subcategory.objects.filter(Q(name='NEWS_GLOBAL_SUB') & Q(parent__name='NEWS'))
          
    context = {
            'global_sub':global_sub
            }
    return render(request, 'subcategories/news_global.html', context)


def africa_sub_news_cat_view(request):
    
    africa_sub = Subcategory.objects.filter(Q(name='NEWS_AFRICA_SUB') & Q(parent__name='NEWS'))
               
    context = {
            'africa_sub':africa_sub, 
            }
    return render(request, 'subcategories/news_africa.html', context)


def opinions_sub_news_cat_view(request):
    opinions_sub = Subcategory.objects.filter(Q(name='NEWS_OPINIONS_SUB') & Q(parent__name='NEWS'))
   
            
    context = {
            'opinions_sub':opinions_sub,
            }
    return render(request, 'subcategories/news_opinions.html', context)



def community_sub_news_cat_view(request):
    
    community_sub = Subcategory.objects.filter(Q(name='NEWS_COMMUNITY_SUB') & Q(parent__name='NEWS'))
   
    context = {
            'community_sub':community_sub
            }
    return render(request, 'subcategories/news_community.html', context)




# politics sub categories

def global_sub_politics_cat_view(request):
    
    global_sub = Subcategory.objects.filter(Q(name='POLITICS_GLOBAL_SUB') & Q(parent__name='POLITICS'))
          
    context = {
            'global_sub':global_sub
            }
    return render(request, 'subcategories/politics_global.html', context)


def africa_sub_politics_cat_view(request):
    
    africa_sub = Subcategory.objects.filter(Q(name='POLITICS_AFRICA_SUB') & Q(parent__name='POLITICS'))
               
    context = {
            'africa_sub':africa_sub, 
            }
    return render(request, 'subcategories/politics_africa.html', context)


def opinions_sub_politics_cat_view(request):
    opinions_sub = Subcategory.objects.filter(Q(name='POLITICS_OPINIONS_SUB') & Q(parent__name='POLITICS'))
   
            
    context = {
            'opinions_sub':opinions_sub,
            }
    return render(request, 'subcategories/politics_opinions.html', context)



def community_sub_politics_cat_view(request):
    
    community_sub = Subcategory.objects.filter(Q(name='POLITICS_COMMUNITY_SUB') & Q(parent__name='POLITICS'))
   
    context = {
            'community_sub':community_sub
            }
    return render(request, 'subcategories/politics_community.html', context)




# business sub categories



def global_sub_business_cat_view(request):
    
    global_sub = Subcategory.objects.filter(Q(name='BUSINESS_GLOBAL_SUB') & Q(parent__name='BUSINESS'))
    
            
    context = {'global_sub':global_sub}
    return render(request, 'subcategories/business_global.html', context)


def igbo_sub_business_cat_view(request):
    
    igbo_sub = Subcategory.objects.filter(Q(name='BUSINESS_IGBO_SUB') & Q(parent__name='BUSINESS'))
   
    context = {'igbo_sub':igbo_sub}
    return render(request, 'subcategories/business_igbo.html', context)
   


def local_sub_business_cat_view(request):
    
    local_sub = Subcategory.objects.filter(Q(name='BUSINESS_LOCAL_SUB') & Q(parent__name='BUSINESS'))
   
            
    context = {'local_sub':local_sub}
    return render(request, 'subcategories/business_local.html', context)
   



# sports sub categories
# 


def global_sub_sports_cat_view(request):
    
    global_sub = Subcategory.objects.filter(Q(name='SPORTS_GLOBAL_SUB') & Q(parent__name='SPORTS'))
            
    context = {'global_sub':global_sub, }
    return render(request, 'subcategories/sports_global.html', context)

def local_sub_sports_cat_view(request):
    
    local_sub = Subcategory.objects.filter(Q(name='SPORTS_LOCAL_SUB') & Q(parent__name='SPORTS'))
   
    context = {'local_sub':local_sub}
    return render(request, 'subcategories/sports_local.html', context)

def communty_sub_sports_cat_view(request):
    
    community_sub = Subcategory.objects.filter(Q(name='SPORTS_COMMUNITY_SUB') & Q(parent__name='SPORTS'))
   
            
    context = {'community_sub':community_sub}
    return render(request, 'subcategories/sports_community.html', context)


# arts sub categories    



def books_sub_arts_cat_view(request):
    
    books_sub = Subcategory.objects.filter(Q(name='ARTS_BOOKS_SUB') & Q(parent__name='ARTS'))
    
            
    context = {
            'books_sub':books_sub
            }
    return render(request, 'subcategories/arts_books.html', context)

def movies_sub_arts_cat_view(request):
    
    movies_sub = Subcategory.objects.filter(Q(name='ARTS_MOVIES_SUB') & Q(parent__name='ARTS'))
    
            
    context = {
            'movies_sub':movies_sub
            }
    return render(request, 'subcategories/arts_movies.html', context)

def music_sub_arts_cat_view(request):
    
    music_sub = Subcategory.objects.filter(Q(name='ARTS_MUSIC_SUB') & Q(parent__name='ARTS'))
    
            
    context = {
            'music_sub':music_sub
            }
    return render(request, 'subcategories/arts_music.html', context)

def showbiz_sub_arts_cat_view(request):
    
    showbiz_sub = Subcategory.objects.filter(Q(name='ARTS_SHOWBIZ_SUB') & Q(parent__name='ARTS'))
            
    context = {
            'showbiz_sub':showbiz_sub
            }
    return render(request, 'subcategories/arts_showbiz.html', context)

def event_sub_arts_cat_view(request):
    
    event_sub = Subcategory.objects.filter(Q(name='ARTS_EVENT_SUB') & Q(parent__name='ARTS'))
   
            
    context = {
            'event_sub':event_sub
            }
    return render(request, 'subcategories/arts_events.html', context)



# lifestyle sub categories


def food_sub_lifestyle_cat_view(request):
    
    food_sub = Subcategory.objects.filter(Q(name='LIFESTYLE_FOOD_SUB') & Q(parent__name='LIFESTYLE'))
            
    context = {
            'food_sub':food_sub
            }
    return render(request, 'subcategories/lifestyle_food.html', context)

def culture_sub_lifestyle_cat_view(request):
    
    culture_sub = Subcategory.objects.filter(Q(name='LIFESTYLE_CULTURE_SUB') & Q(parent__name='LIFESTYLE'))
            
    context = {
            'culture_sub':culture_sub
            }
    return render(request, 'subcategories/lifestyle_culture.html', context)

def fashion_sub_lifestyle_cat_view(request):
    
    fashion_sub = Subcategory.objects.filter(Q(name='LIFESTYLE_FASHION_SUB') & Q(parent__name='LIFESTYLE'))
            
    context = {
            'fashion_sub':fashion_sub
           }
    return render(request, 'subcategories/lifestyle_fashion.html', context)

def travel_sub_lifestyle_cat_view(request):
    
    travel_sub = Subcategory.objects.filter(Q(name='LIFESTYLE_TRAVEL_SUB') & Q(parent__name='LIFESTYLE'))
        
    context = {
            'travel_sub':travel_sub,
            }
    return render(request, 'subcategories/lifestyle_travel.html', context)

def opinions_sub_lifestyle_cat_view(request):
    
    opinions_sub = Subcategory.objects.filter(Q(name='LIFESTYLE_OPINIONS_SUB') & Q(parent__name='LIFESTYLE'))

   
            
    context = {
            'opinions_sub':opinions_sub
            }
    return render(request, 'subcategories/lifestyle_opinions.html', context)



# scitech subcategories


def global_sub_scitech_cat_view(request):
    
    global_sub = Subcategory.objects.filter(Q(name='SCITECH_GLOBAL_SUB') & Q(parent__name='SCITECH'))
            
    context = {
            'global_sub':global_sub
            }
    return render(request, 'subcategories/scitech_global.html', context)

def digitech_fintech_sub_scitech_cat_view(request):    
    digfintech_sub = Subcategory.objects.filter(Q(name='SCITECH_DIGFINTECH_SUB') & Q(parent__name='SCITECH'))
            
    context = {
            'digfintech_sub':digfintech_sub,
            }
    return render(request, 'subcategories/scitech_digital_fintech.html', context)

def  blockchain_sub_scitech_cat_view(request):
    
    blockchain_sub = Subcategory.objects.filter(Q(name='SCITECH_BLOCKCHAIN_SUB') & Q(parent__name='SCITECH'))
            
    context = {
             'blockchain_sub':blockchain_sub
            }
    return render(request, 'subcategories/scitech_blockchain.html', context)

def crypto_sub_scitech_cat_view(request):
    
    crypto_sub = Subcategory.objects.filter(Q(name='SCITECH_CRYPTO_SUB') & Q(parent__name='SCITECH'))
            
    context = {
            ' crypto_sub': crypto_sub
            }
    return render(request, 'subcategories/scitech_crypto.html', context)

def ntf_sub_scitech_cat_view(request):
    
    ntf_sub = Subcategory.objects.filter(Q(name='SCITECH_NTF_SUB') & Q(parent__name='SCITECH'))
                
    context = {
             'ntf_sub':ntf_sub
            }
    return render(request, 'subcategories/scitech_ntf.html', context)

def web3_sub_scitech_cat_view(request):
    
    web3_sub = Subcategory.objects.filter(Q(name='SCITECH_WEB3_SUB') & Q(parent__name='SCITECH'))
   
   
   
            
    context = {
             'web3_sub':web3_sub
            }
    return render(request, 'subcategories/scitech_web3.html', context)

def community_sub_scitech_cat_view(request):
    
    community_sub = Subcategory.objects.filter(Q(name='SCITECH_COMMUNITY_SUB') & Q(parent__name='SCITECH'))
   
    context = {
             'community_sub': community_sub
            }
    return render(request, 'subcategories/scitech_community.html', context)



# health sub categories

def global_sub_health_cat_view(request):
    
    global_sub = Subcategory.objects.filter(Q(name='HEALTH_GLOBAL_SUB') & Q(parent__name='HEALTH'))
    
    context = {'global_sub':global_sub}
    return render(request, 'subcategories/health_global.html', context)


def local_sub_health_cat_view(request):
    
    local_sub = Subcategory.objects.filter(Q(name='HEALTH_LOCAL_SUB') & Q(parent__name='HEALTH'))
          
    context = {'local_sub':local_sub}
    return render(request, 'subcategories/health_local.html', context)


def opinions_sub_health_cat_view(request):

    opinions_sub = Subcategory.objects.filter(Q(name='HEALTH_OPINIONS_SUB') & Q(parent__name='HEALTH'))
   
            
    context = {'opinions_sub':opinions_sub}
    return render(request, 'subcategories/health_opinions.html', context)


def community_sub_health_cat_view(request):
    
    community_sub = Subcategory.objects.filter(Q(name='HEALTH_COMMUNITY_SUB') & Q(parent__name='HEALTH'))
               
    context = {'community_sub':community_sub}
    return render(request, 'subcategories/health_community.html', context)


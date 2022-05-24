from django.urls import include, path
from django.conf.urls import url



from ibmn.categories.views.categories_views import (
                                    news_cat_view, politics_cat_view, business_cat_view, sports_cat_view,
                                    health_cat_view, arts_cat_view, lifestyle_cat_view, scitech_cat_view
                                    
                                    )


from ibmn.categories.views.subcategories_views import ( 
                                 global_sub_news_cat_view, community_sub_news_cat_view, opinions_sub_news_cat_view, 
                                 africa_sub_news_cat_view, global_sub_politics_cat_view, community_sub_politics_cat_view, 
                                 opinions_sub_politics_cat_view, africa_sub_politics_cat_view,global_sub_business_cat_view, local_sub_business_cat_view,
                                 igbo_sub_business_cat_view, global_sub_sports_cat_view, local_sub_sports_cat_view,
                                 communty_sub_sports_cat_view, books_sub_arts_cat_view, movies_sub_arts_cat_view,
                                 music_sub_arts_cat_view, showbiz_sub_arts_cat_view, event_sub_arts_cat_view,
                                 food_sub_lifestyle_cat_view, culture_sub_lifestyle_cat_view,fashion_sub_lifestyle_cat_view,
                                 opinions_sub_lifestyle_cat_view, travel_sub_lifestyle_cat_view , global_sub_scitech_cat_view,
                                 web3_sub_scitech_cat_view, blockchain_sub_scitech_cat_view, ntf_sub_scitech_cat_view, crypto_sub_scitech_cat_view,
                                 community_sub_scitech_cat_view, digitech_fintech_sub_scitech_cat_view, global_sub_health_cat_view,
                                 local_sub_health_cat_view, opinions_sub_health_cat_view , community_sub_health_cat_view
                               
                               )


app_name = "categories"
urlpatterns = [
    path('news/', view=news_cat_view, name="news"),
    path('politics/', view=politics_cat_view, name="politics"),
    path('business/', view=business_cat_view, name="business"),
    path('sports/', view=sports_cat_view, name="sports"),
    path('health/', view=health_cat_view, name="health"),
    path('arts/', view=arts_cat_view, name="arts"),
    path('lifestyle/', view=lifestyle_cat_view, name="lifestyle"),
    path('scitech/', view=scitech_cat_view, name="scitech"),
    path('news/global/', view=global_sub_news_cat_view, name="news_global"),
    path('news/community/', view=community_sub_news_cat_view, name="news_community"),
    path('news/opinions/', view=opinions_sub_news_cat_view, name="news_opinions"),
    path('news/africa/', view=africa_sub_news_cat_view, name="news_africa"),
    path('politics/global/', view=global_sub_politics_cat_view, name="politics_global"),
    path('politics/community/', view=community_sub_politics_cat_view, name="politics_community"),
    path('politics/africa/', view=africa_sub_politics_cat_view, name="politics_africa"),
    path('politics/opinions/', view=opinions_sub_politics_cat_view, name="politics_opinions"),
    path('business/global/', view=global_sub_business_cat_view, name="business_global"),
    path('business/igbo/', view=igbo_sub_business_cat_view, name="business_igbo"),
    path('business/local/', view=local_sub_business_cat_view, name="business_local"),
    path('sports/global/', view=global_sub_sports_cat_view, name="sports_global"),
    path('sports/local/', view=local_sub_sports_cat_view, name="sports_local"),
    path('sports/community/', view=communty_sub_sports_cat_view, name="sports_community"),
    path('arts/books/', view=books_sub_arts_cat_view, name="arts_books"),
    path('arts/music/', view=music_sub_arts_cat_view, name="arts_music"),
    path('arts/movies/', view=movies_sub_arts_cat_view, name="arts_movies"),
    path('arts/showbiz/', view=showbiz_sub_arts_cat_view, name="arts_showbiz"),
    path('arts/events/', view=event_sub_arts_cat_view, name="arts_events"),
    path('lifestyle/food/', view=food_sub_lifestyle_cat_view, name="lifestyle_food"),
    path('lifestyle/culture/', view=culture_sub_lifestyle_cat_view, name="lifestyle_culture"),
    path('lifestyle/travel/', view=travel_sub_lifestyle_cat_view, name="lifestyle_travel"),
    path('lifestyle/fashion/', view=fashion_sub_lifestyle_cat_view, name="lifestyle_fashion"),
    path('lifestyle/opinions/', view=opinions_sub_lifestyle_cat_view, name="lifestyle_opinions"),
    path('scitech/blockchain/', view=blockchain_sub_scitech_cat_view, name="scitech_blockchain"),
    path('scitech/ntf/', view=ntf_sub_scitech_cat_view, name="scitech_ntf"),
    path('scitech/crypto/', view=crypto_sub_scitech_cat_view, name="scitech_crypto"),
    path('scitech/web3/', view=web3_sub_scitech_cat_view, name="scitech_web3"),
    path('scitech/global/', view=global_sub_scitech_cat_view, name="scitech_global"),
    path('scitech/digitech_fintech/', view=digitech_fintech_sub_scitech_cat_view, name="scitech_digitech_fintech"),
    path('scitech/community/', view=community_sub_scitech_cat_view, name="scitech_community"),
    path('health/local/', view=local_sub_health_cat_view, name="health_local"),
    path('health/global/', view=global_sub_health_cat_view, name="health_global"),
    path('health/opinions/', view=opinions_sub_health_cat_view, name="health_opinions"),
    path('health/community/', view=community_sub_health_cat_view, name="health_community"),
    
   
]
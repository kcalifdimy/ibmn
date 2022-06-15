from django.urls import include, path
from django.conf.urls import url


from ibmn.trending.views import (TrendCreateView, trend_update_view, trend_list_view,
                                  trending_news_details_view,trend_manager_delete_view ,
                                  trending_news_reply_page
                                 )


app_name = "trending"
urlpatterns = [
    path("create/", TrendCreateView.as_view(), name="trending_create"),
    path('list_trend/', view=trend_list_view, name='trend_list_post'),
    path('update/<uuid:uuid>/', view=trend_update_view, name='trend_update_news'),
    path('delete/<uuid:uuid>/', view=trend_manager_delete_view, name='trend_delete_news'),
    path("<slug:slug>/", view=trending_news_details_view, name="trendnews_detail"),
    path('trend_comment/reply/', trending_news_reply_page, name="trendnews_reply"),


    #path("<slug:slug>/", view=news_detail_view, name="news_detail"),

]


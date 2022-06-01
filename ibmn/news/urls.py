from django.urls import include, path
from django.conf.urls import url


from ibmn.news.views import (
                            home_view , manager_home_view, news_create_view,  manager_list_post_view, 
                             manager_update_view, manager_delete_view, news_details_view, reply_page,
                             search_list_news_view
                            )


app_name = "news"
urlpatterns = [
    path('', view=home_view, name="home"),
    path("create_news/", view=news_create_view, name="create"),
    path('list/', view=manager_list_post_view, name='manager_list_post'),
    path("home/", view= manager_home_view, name="manager_home"),
    path('update/<uuid:uuid>/', view=manager_update_view, name='manager_update_news'),
    path('delete/<uuid:uuid>/', view=manager_delete_view, name='manager_delete_news'),
    #path("<slug:tag_slug>/", view=news_details_view, name="news_tag_detail"),
    path("<slug:slug>/", view=news_details_view, name="news_detail"),
    path('comment/reply/', reply_page, name="reply"),
    path('list/', view=search_list_news_view, name='search'),


]
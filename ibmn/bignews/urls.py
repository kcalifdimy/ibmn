from django.urls import include, path
from django.conf.urls import url


from ibmn.bignews.views import (bignews_create_view, bignews_update_view, big_news_details_view,
                                bignews_manager_delete_view , bignews_list_view, big_news_reply_page)


app_name = "bignews"
urlpatterns = [
    path("create/", view=bignews_create_view, name="bignews_create"),
    path('list_news/', view=bignews_list_view, name='bignews_list_post'),
    path('update/<uuid:uuid>/', view=bignews_update_view, name='bignews_update_news'),
    path('delete/<uuid:uuid>/', view= bignews_manager_delete_view, name='bignews_delete_news'),
    path("<slug:slug>/", view=big_news_details_view, name="bignews_detail"),
    path('big_comment/reply/', big_news_reply_page, name="bignews_reply"),



]
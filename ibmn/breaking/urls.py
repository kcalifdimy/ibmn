from django.urls import include, path
from django.conf.urls import url


from ibmn.breaking.views import ( break_list_view, break_create_view,
                                 break_update_view, breaking_manager_delete_view)


app_name = "breaking"
urlpatterns = [
    path("create/", view=break_create_view, name="break_create"),
    path('list/', view=break_list_view, name='break_list'),
    path('update/<uuid:uuid>/', view=break_update_view, name='break_update_news'),
    path('delete/<uuid:uuid>/', view=breaking_manager_delete_view, name='break_delete_news'),

    #path("<slug:slug>/", view=news_detail_view, name="news_detail"),

]
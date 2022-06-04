from django.urls import path
from ibmn.users.views import LoginView, logout_view



app_name = "users"
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', view=logout_view, name='logout'),

    
]
from django.urls import path,include
from . import views

app_name='app1'

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('about',views.about,name='about'),
    path('login',views.login,name='login'),
]
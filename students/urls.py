from django.urls import path
from . import views

app_name='students'

urlpatterns = [
    path('studenthome',views.student_home,name='studenthome'),
    path('studentprofile',views.student_profile,name='studentprofile')
]
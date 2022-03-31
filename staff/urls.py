from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('staffhome',views.teacher_home,name='staffhome'),
    path('profile',views.profile,name='profile'),
    path('studentlist/<int:id>',views.student_list,name='studentlists')
]

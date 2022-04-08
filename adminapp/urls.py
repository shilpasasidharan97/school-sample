from django.urls import path, include
from . import views

app_name = 'adminapp'

urlpatterns = [
    path('home', views.home, name='home'),
    path('addteacher', views.add_teacher, name='addteacher'),
    path('manageteacher', views.manage_teacher, name='manageteacher'),
    path('deleteteacher/<int:tid>',views.delete_teacher,name='deleteteacher'),
    path('addstudent', views.add_student, name='addstudent'),
    path('managestudent', views.manage_student, name='managestudent'),
    path('deletestudent/<int:sid>',views.delete_student,name='deletestudent'),
    path('addparents', views.add_parents, name='addparents'),
    path('manageparents', views.manage_parents, name='manageparents'),
    path('addclass', views.add_class, name='addclass'),
    path('classlist', views.class_list, name='classlist'),
    path('deleteclass/<int:cid>',views.delete_class,name='deleteclass'),
    path('logout',views.logout,name='logout'),
    path('changepassword',views.change_password,name="changepassword"),
]

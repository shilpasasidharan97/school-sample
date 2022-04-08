from django.urls import path
from . import views

app_name = 'staff'

urlpatterns = [
    path('staffhome',views.teacher_home,name='staffhome'),
    path('profile',views.profile,name='profile'),
    path('studentlist',views.student_list,name='studentlists'),
    path('logout',views.logout,name='logout'),
    path('attendance',views.attendance,name='attendance'),
    # path('present',views.present,name='present'),
    # path('halfday',views.half_day,name='halfday'),
    # path('absent',views.absent,name='absent'),
    path('mark',views.mark,name='mark'),
    # path('changepassword',views.change_password,name='changepassword')
]

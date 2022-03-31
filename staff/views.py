from django.shortcuts import render

from adminapp.models import StudentDetails, TeacherBasic

# Create your views here.

def teacher_home(request):

    teacher=TeacherBasic.objects.get(t_id =  request.session['teacher'])
    return render(request,'staffhome.html',{'teacher':teacher,})

def profile(request):
    profile=TeacherBasic.objects.filter(t_id =  request.session['teacher'])
    return render(request,'profile.html',{'profile':profile,})

def student_list(request,id):

    # students_data=StudentDetails.objects.filter()
    return render(request,'student_list.html')
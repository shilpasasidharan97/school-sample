from django.shortcuts import render

from adminapp.models import StudentDetails

# Create your views here.

def student_home(request):
    student=StudentDetails.objects.get(s_id=request.session['student'])
    return render(request,'student_home.html',{'student':student,})

def student_profile(request):
    student_data=StudentDetails.objects.filter(s_id=request.session['student'])
    return render(request,'student_profile.html',{'student':student_data,})
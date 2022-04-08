from django.shortcuts import redirect, render

from adminapp.models import StudentDetails, TeacherBasic
from staff.models import Attendance

# Create your views here.

def teacher_home(request):

    teacher=TeacherBasic.objects.get(t_id =  request.session['teacher'])
    return render(request,'staffhome.html',{'teacher':teacher,})

def profile(request):
    profile=TeacherBasic.objects.filter(t_id =  request.session['teacher'])
    return render(request,'profile.html',{'profile':profile,})



def student_list(request):
    teacher = TeacherBasic.objects.get(t_id=request.session['teacher'])
    classes=teacher.classlist
    students = StudentDetails.objects.filter(classes=classes)

    return render(request,'student_list.html',{'student':students,})


def change_password(request):
    msg=""
    if request.method=='POST':
        old_psw=request.POST['oldPassword']
        new_psw=request.POST['password']
        c_psw=request.POST['confirmPassword']
        staff_data=TeacherBasic.objects.get(t_id=request.session['teacher'])

        if staff_data.dob==old_psw:
            if new_psw==c_psw:
                TeacherBasic.objects.filter(t_id=request.session['admin']).update(dob=new_psw)
                msg="successfully reset the password"
            else:
                msg="Mismatch"
        else:
            msg="Incorrect password.."
    return render(request,'changepassword.html',{'msg':msg,})



def logout(request):
    del request.session['teacher']
    request.session.flush()
    return redirect('app1:login')


def attendance(request):

    if request.method=='POST':
        date=request.POST['date']
        student=request.POST['sid']
        student_id = StudentDetails.objects.get(s_id=student)

        if 'present' in request.POST:
            status="p"
            attendance=Attendance(student=student_id,date=date,status=status)
            attendance.save()
        elif 'halfday' in request.POST:
            status="h"
            attendance=Attendance(student=student_id,date=date,status=status)
            attendance.save()
        else:
            status="a"
            attendance=Attendance(student=student_id,date=date,status=status)
            attendance.save()

            
    teacher = TeacherBasic.objects.get(t_id=request.session['teacher'])
    classes=teacher.classlist
    students = StudentDetails.objects.filter(classes=classes)
    return render(request,'attendance.html',{'students':students,})


# def present(request):
#     return redirect('staff:attendance')


# def half_day(request):
#     return redirect('staff:attendance')


# def absent(request):
#     return redirect('staff:attendance')


def mark(request):
    return render(request,'mark.html')
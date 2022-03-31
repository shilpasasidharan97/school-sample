from django.shortcuts import redirect, render

from adminapp.models import AdminDetails, StudentDetails, TeacherBasic

# Create your views here.


def homepage(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    msg = ""
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['psw']
#  also do admin student and parents login

        staff_exist = TeacherBasic.objects.filter(email_id=username, dob=password)
        student_exist = StudentDetails.objects.filter(email_id=username, dob=password)
        admin_exist = AdminDetails.objects.filter(username=username, password=password)

        if staff_exist:
            staff_data = TeacherBasic.objects.get(email_id=username, dob=password)
            request.session['teacher'] = staff_data.t_id
            return redirect('staff:staffhome')

        elif admin_exist:
            admin_data = AdminDetails.objects.get(username=username, password=password)
            request.session['admin'] = admin_data.admin_id
            return redirect('adminapp:home')

        elif student_exist:
            student_data = StudentDetails.objects.get(email_id=username, dob=password)
            request.session['student'] = student_data.s_id
            return redirect('students:studenthome')

        else:
            msg = "username or password is error"
            return render(request, 'erp-login.html', {'msg': msg, })

    return render(request, 'erp-login.html')


from django.shortcuts import redirect, render

from adminapp.models import AdminDetails, ClassList, ClassSchedule, StudentDetails, TeacherBasic



# Create your views here.


def home(request):
    admins=AdminDetails.objects.get(admin_id =  request.session['admin'])

    return render(request, 'home.html',{'admin':admins,})


def add_teacher(request):
    msg=""
    if request.method=='POST':
        profile=request.FILES['profile']
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        age=request.POST['age']
        religion=request.POST['religion']
        cast=request.POST['cast']
        place=request.POST['place']
        dist=request.POST['dist']
        nationality=request.POST['nationality']
        adddhar=request.POST['aadhar']
        email=request.POST['email']
        phone_number=request.POST['phn']
        handling_class=request.POST['class']
        division=request.POST['division']
        subject=request.POST['sub']
        qualification=request.POST['qualification']
        college_name=request.POST['cname']
        quali_certificate=request.FILES['doc1']
        institution_name=request.POST['iname']
        year_of_experience=request.POST['exp']
        exp_certificate=request.FILES['doc2']

        email_exists = TeacherBasic.objects.filter(email_id=email).exists()


        if not email_exists:
            new_teacher=TeacherBasic(t_name=name,gender=gender,dob=dob,age=age,religion=religion,cast=cast,place=place,district=dist,nationality=nationality,aadhar_num=adddhar,email_id=email,phone_number=phone_number,handling_class=handling_class,division=division,subject=subject,qualification=qualification,college_name=college_name,quali_certificate=quali_certificate,instituation_name=institution_name,year_of_experience=year_of_experience,experience_certificate= exp_certificate,t_profile=profile)
            new_teacher.save()
            msg = "New teacher added Successfully"
        else:
            msg = "Email already exists"

    return render(request, 'add_teacher.html',{'msg':msg})


def manage_teacher(request):

    teachers=TeacherBasic.objects.all()
    return render(request, 'manage_teacher.html',{'teachers':teachers,})

def delete_teacher(request,tid):
    teacher=TeacherBasic.objects.get(t_id=tid)
    teacher.delete()
    return redirect('adminapp:manageteacher')


def add_student(request):
    msg=""
    if request.method=='POST':
        profile=request.FILES['profile']
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        age=request.POST['age']
        religion=request.POST['religion']
        cast=request.POST['cast']
        place=request.POST['place']
        dist=request.POST['dist']
        nationality=request.POST['nationality']
        aadhar=request.POST['aadhar']
        email=request.POST['email']
        phone_number=request.POST['phn']
        reg_num=request.POST['regnum']
        classs=request.POST['class']
        division=request.POST['division']
        father_name=request.POST['fname']
        mother_name=request.POST['mname']
        father_occu=request.POST['focc']
        mother_occu=request.POST['mocc']
        parent_phone=request.POST['pphn']
        parent_email=request.POST['pemail']
        address=request.POST['address']

        email_exists = StudentDetails.objects.filter(email_id=email).exists()
        if not email_exists:
            new_student=StudentDetails(s_profile=profile,s_name=name,gender=gender,dob=dob,age=age,religion=religion,cast=cast,place=place,district=dist,nationality=nationality,aadhar_num=aadhar,email_id=email,phone_number=phone_number,registration_num=reg_num,classs=classs,division=division,father_name=father_name,mother_name=mother_name,father_occupation=father_occu,mother_occupation=mother_occu,parents_phone=parent_phone,parents_email=parent_email,address=address)
            new_student.save()
            msg="New student added successfully"
        else:
            msg="The student is already exists"

    return render(request, 'add_student.html',{'msg':msg,})


def manage_student(request):
    students=StudentDetails.objects.all().order_by('classs','division')
    return render(request, 'manage_student.html',{'students':students,})


def delete_student(request,sid):
    student=StudentDetails.objects.get(s_id=sid)
    student.delete()
    return redirect('adminapp:managestudent')


def add_parents(request):
    return render(request, 'add_parents.html')


def manage_parents(request):
    return render(request, 'manage_parents.html')


def add_class(request):
    msg=""
    if request.method=='POST':
        classs=request.POST['class']
        divisions=request.POST['division']
        strength=request.POST['strength']

        class_exist=ClassList.objects.filter(classes=classs,division=divisions).exists()
        if not class_exist:
            new_class=ClassList(classes=classs,division=divisions,strength=strength)
            new_class.save()
            msg="Class added successfully"

        else:
            msg="Class already exist"


    classes=ClassList.objects.all().order_by('classes','division')
    
    return render(request, 'add_class.html',{'msg':msg,'class':classes})


def class_list(request):

    classschedule=ClassSchedule.objects.all()
    return render(request, 'class_list.html',{'classschedule':classschedule,})

def logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect('app1:login')


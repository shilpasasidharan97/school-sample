
from django.shortcuts import redirect, render
import random  #to generate random numbers 
from adminapp.models import AdminDetails, ClassList, StudentDetails, TeacherBasic



# Create your views here.


def home(request):
    
    admins=AdminDetails.objects.get(admin_id =  request.session['admin'])
    return render(request, 'home.html',{'admin':admins,})


def add_teacher(request):

    msg=""
    year_of_experience=0
    exp_certificate=""
    # profile=""
     
    classes=ClassList.objects.all()
    
    if request.method=='POST':
        profile=request.FILES['profile']
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        age=request.POST['age']
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

        clases = ClassList.objects.get(classes=handling_class, division=division)
        if request.POST['exp']:
            year_of_experience=request.POST['exp']

        if request.POST['doc2']:
            exp_certificate=request.FILES['doc2']
        
        # if request.POST['profile']:
            # profile=request.FILES['profile']
        
        email_exists = TeacherBasic.objects.filter(email_id=email).exists()
        
        if not email_exists:
            new_teacher=TeacherBasic(t_name=name,gender=gender,dob=dob,age=age,place=place,district=dist,nationality=nationality,aadhar_num=adddhar,email_id=email,phone_number=phone_number,subject=subject,qualification=qualification,college_name=college_name,quali_certificate=quali_certificate,instituation_name=institution_name,year_of_experience=year_of_experience,experience_certificate= exp_certificate,t_profile=profile,classlist=clases)
            new_teacher.save()
            msg = "New teacher added Successfully"
        else:
            msg = "Teacher already exists"

    return render(request, 'add_teacher.html',{'msg':msg,'classes':classes})



def manage_teacher(request):
    teachers=TeacherBasic.objects.all()
    return render(request, 'manage_teacher.html',{'teachers':teachers,})


def delete_teacher(request,tid):
    teacher=TeacherBasic.objects.get(t_id=tid)
    teacher.delete()
    return redirect('adminapp:manageteacher')


def add_student(request):
    # rand=random.randint(10000,999999)
    # reg_no='RP'+str(rand)
    # print(reg_no)

    # profile=""
    msg=""
    reg_no=""

    rand=random.randint(10000,999999)
    reg_no='RP'+str(rand)

    clases=ClassList.objects.all()

    if request.method=='POST':
        profile=request.FILES['profile']
        name=request.POST['name']
        gender=request.POST['gender']
        dob=request.POST['dob']
        age=request.POST['age']
        place=request.POST['place']
        dist=request.POST['dist']
        nationality=request.POST['nationality']
        aadhar=request.POST['aadhar']
        email=request.POST['email']
        phone_number=request.POST['phn']
        classs=request.POST['class']
        division=request.POST['division']
        father_name=request.POST['fname']
        mother_name=request.POST['mname']
        father_occu=request.POST['focc']
        mother_occu=request.POST['mocc']
        parent_phone=request.POST['pphn']
        parent_email=request.POST['pemail']
        address=request.POST['address']
        registration_num=reg_no


        # if request.POST['profile']:
        #     profile=request.FILES['profile']

        classes=ClassList.objects.get(classes=classs,division=division)

        email_exists = StudentDetails.objects.filter(email_id=email).exists()
        
        if not email_exists:
            new_student=StudentDetails(s_profile=profile,s_name=name,gender=gender,dob=dob,age=age,place=place,district=dist,nationality=nationality,aadhar_num=aadhar,email_id=email,phone_number=phone_number,father_name=father_name,mother_name=mother_name,father_occupation=father_occu,mother_occupation=mother_occu,parents_phone=parent_phone,parents_email=parent_email,address=address,registration_num=registration_num,classes=classes)
            new_student.save()
            msg="New student added successfully"
        else:
            msg="The student is already exists"

    
        # reg_number=StudentDetails(registration_num=reg_no)

    return render(request, 'add_student.html',{'msg':msg,'reg_no':reg_no,'classes':clases})


def manage_student(request):
    students=StudentDetails.objects.all().order_by('classes')
    
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

    classlist=TeacherBasic.objects.all()
    return render(request, 'class_list.html',{'classlist':classlist,})






def delete_class(request,cid):
    classes=ClassList.objects.get(c_id=cid)
    classes.delete()
    return redirect('adminapp:addclass')

def logout(request):
    del request.session['admin']
    request.session.flush()
    return redirect('app1:login')


def change_password(request):
    msg=""
    if request.method=='POST':
        old_psw=request.POST['oldPassword']
        new_psw=request.POST['password']
        c_psw=request.POST['confirmPassword']
        admin_data=AdminDetails.objects.get(admin_id=request.session['admin'])

        if admin_data.password==old_psw:
            if new_psw==c_psw:
                AdminDetails.objects.filter(admin_id=request.session['admin']).update(password=new_psw)
                msg="successfully reset the password"
            else:
                msg="Mismatch"
        else:
            msg="Incorrect password.."
    return render(request,'change_password.html',{'msg':msg,})

from __future__ import division
from datetime import datetime
from distutils.command.upload import upload
import email
from django.db import models

# Create your models here.

class TeacherBasic(models.Model):
    t_id=models.AutoField(primary_key=True)
    t_profile=models.ImageField(upload_to='teachers/')
    t_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=7)
    dob=models.DateField()
    age=models.IntegerField()
    religion=models.CharField(max_length=15)
    cast=models.CharField(max_length=10)
    place=models.CharField(max_length=20)
    district=models.CharField(max_length=20,default="")
    nationality=models.CharField(max_length=20)
    aadhar_num=models.CharField(max_length=15)
    email_id=models.CharField(max_length=25)
    phone_number=models.CharField(max_length=15)
    handling_class=models.IntegerField()
    division=models.CharField(max_length=2,default="")
    subject=models.CharField(max_length=15)
    qualification=models.CharField(max_length=30)
    college_name=models.CharField(max_length=50)
    quali_certificate=models.FileField(upload_to='teachers/',blank= True,null = True)
    instituation_name=models.CharField(max_length=50,blank= True,null = True)
    year_of_experience=models.IntegerField(blank= True,null = True)
    experience_certificate=models.FileField(upload_to='teachers/',null = True)

    class Meta:
        db_table='teachers'

class AdminDetails(models.Model):
    admin_id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10,default="")

    class Meta:
        db_table='adminlogin'


class StudentDetails(models.Model):
    s_id=models.AutoField(primary_key=True)
    s_profile=models.ImageField(upload_to='students/')
    s_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=7)
    dob=models.DateField()
    age=models.IntegerField()
    religion=models.CharField(max_length=15)
    cast=models.CharField(max_length=10)
    place=models.CharField(max_length=20)
    district=models.CharField(max_length=20)
    nationality=models.CharField(max_length=20)
    aadhar_num=models.CharField(max_length=20)
    email_id=models.CharField(max_length=25)
    phone_number=models.CharField(max_length=20)
    registration_num=models.IntegerField()
    classs=models.IntegerField()
    division=models.CharField(max_length=1)
    father_name=models.CharField(max_length=20)
    father_occupation=models.CharField(max_length=20,blank= True,null = True)
    mother_name=models.CharField(max_length=20)
    mother_occupation=models.CharField(max_length=20,blank= True,null = True)
    parents_phone=models.CharField(max_length=20)
    parents_email=models.CharField(max_length=30)
    address=models.CharField(max_length=60,blank= True,null = True)

    class Meta:
        db_table='students'

class ClassList(models.Model):
    c_id=models.AutoField(primary_key=True)
    classes=models.IntegerField()
    division=models.CharField(max_length=2)
    strength=models.IntegerField(default=0)

    class Meta:
        db_table='classes'


class ClassSchedule(models.Model):
    teacher=models.ForeignKey(TeacherBasic,on_delete=models.CASCADE)
    classes=models.ForeignKey(ClassList,on_delete=models.CASCADE)

    class Meta:
        db_table='scheduledclass'

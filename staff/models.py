from django.db import models
from datetime import datetime

from adminapp.models import ClassList, StudentDetails, TeacherBasic

# Create your models here.

class StudentsUnderStaff(models.Model):
    id=models.AutoField(primary_key=True)
    classes=models.ForeignKey(ClassList,on_delete=models.CASCADE)
    teachers=models.ForeignKey(TeacherBasic,on_delete=models.CASCADE)
    students=models.ForeignKey(StudentDetails,on_delete=models.CASCADE)

    class Meta:
        db_table='studentsunderme'


class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    student=models.ForeignKey(StudentDetails,on_delete=models.CASCADE)
    date=models.DateField(blank=True, default='', null=True)
    status=models.CharField(max_length=5)

    class Meta:
        db_table='attendance'
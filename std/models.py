from django.contrib.auth.models import AbstractUser
from django.db import models

#class tbl_checklogin(models.Model):
  #  username = models.CharField(max_length=100, null=True)
   # password = models.CharField(max_length=100, null=True)


class tbl_courses(models.Model):
   Course_name = models.CharField(max_length=100, null=True)
   Duration = models.CharField(max_length=100, null=True)
   fees = models.CharField(max_length=100, null=True)
   Instructor = models.CharField(max_length=100, null=True)
   description = models.CharField(max_length=100, null=True)

class tbl_teachers(models.Model):
   Name = models.CharField(max_length=100, null=True)
   Email = models.EmailField(null=True)
   Phone = models.CharField(max_length=100, null=True)
   Subject_Taught = models.CharField(max_length=100, null=True)
   Grade_Level = models.CharField(max_length=100, null=True)
   Years_of_Experience=  models.CharField(max_length=100, null=True)
   Additional_Information = models.CharField(max_length=100, null=True)

class tbl_application_form(models.Model):
  course=models.ForeignKey(tbl_courses,on_delete=models.CASCADE,null=True)
  name = models.CharField(max_length=100,null=True)
  email = models.EmailField(null=True)
  phone = models.CharField(max_length=15,null=True)
  gender = models.CharField(max_length=10,null=True)
  address = models.CharField(max_length=10,null=True)
  terms = models.CharField(max_length=10,null=True)



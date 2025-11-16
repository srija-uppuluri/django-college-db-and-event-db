from django.db import models

# from django.db import models

"""class Student(models.Model):
    name=models.CharField(max_length=40)
    usn=models.CharField(max_length=10)
    cgpa=models.FloatField()
    branch=models.CharField(max_length=10)
    gender=models.CharField(max_length=10)
    phone=models.BigIntegerField()

class Professor(models.Model):
    name=models.CharField(max_length=40)
    professor_id=models.CharField(max_length=10)
    experience=models.FloatField()
    branch=models.CharField(max_length=10)
    subject=models.CharField(max_length=15)
    gender=models.CharField(max_length=10)
    phone=models.BigIntegerField()"""

class  Student(models.Model):
    usn=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.CharField(max_length=100)

class Subject(models.Model):
    Subject_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)

class Enrollments(models.Model):
    enroll_id=models.AutoField(primary_key=True)
    usn=models.ForeignKey(Student,on_delete=models.CASCADE)
    Subject_id=models.ForeignKey(Subject,on_delete=models.CASCADE)
    

 

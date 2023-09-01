from django.db import models

# Create your models here.

class School(models.Model):
    Scname=models.CharField(max_length=100,primary_key=True)
    Scprincipal=models.CharField(max_length=100)
    Sclocation=models.CharField(max_length=100)

    def __str__(self):
        return self.Scname
    
class Student(models.Model):
    Scname=models.ForeignKey(School,on_delete=models.CASCADE)
    Sname=models.CharField(max_length=100)
    Sid=models.IntegerField(primary_key=True)

    def __str__(self):
        return self.Sname
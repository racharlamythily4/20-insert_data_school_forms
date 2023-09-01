from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse
def insert_school(request):

    if request.method=='POST':
        scn=request.POST['scn']
        scp=request.POST['scp']
        scl=request.POST['scl']

        SO=School.objects.get_or_create(Scname=scn,Scprincipal=scp,Sclocation=scl)[0]
        SO.save()
        QSSO=School.objects.all()
        d={'QSSO':QSSO}
        return render(request,'display_school.html',d)

    return render(request,'insert_school.html')

def insert_student(request):
    
    if request.method=='POST':
        scn=request.POST['scn']
        sn=request.POST['sn']
        si=request.POST['si']

        STO=School.objects.get(Scname=scn)
        ST=Student.objects.get_or_create(Scname=STO,Sname=sn,Sid=si)[0]
        ST.save()

        QSO=Student.objects.all()
        d={'QSO':QSO}

        return render(request,'display_student.html',d)

    return render(request,'insert_student.html')
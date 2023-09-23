from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from app.models import *
# Create your views here.

def insert_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            Sname=SFDO.cleaned_data['Sname']
            Sid=SFDO.cleaned_data['Sid']
            Email=SFDO.cleaned_data['Email']
            SO=Student.objects.get_or_create(Sname=Sname,Sid=Sid,Email=Email)[0]
            SO.save()
            QSSO=Student.objects.all()
            d1={'QSSO':QSSO}
            return render(request,'display_student.html',d1)
        else:
            return HttpResponse('INVALID DATA')
    return render(request,'insert_student.html',d)
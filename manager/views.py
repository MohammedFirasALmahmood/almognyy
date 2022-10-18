from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from rest_framework.decorators import api_view

# Create your views here.


def Manage(request):
    return render(request,'manager/manage.html')


def ADD(request):
    if request.method=="POST":
        student_name=request.POST.get("name")
        student_phone=request.POST.get("number")
        student_balance=request.POST.get("balance")
        date=Student(student_name=student_name,student_phone=student_phone,student_balance=student_balance)
        date.save()
    return render(request,'manager/addstudent.html')


def GetCode(request):
    list1 = {}
    if request.method == "POST":
        student_phone = request.POST.get("number")
        list = Student.objects.get(student_phone=student_phone)
        return render(request, 'manager/GetCode.html',{'list':list})
    return render(request, 'manager/GetCode.html',list1)


def Charge(request):
    if request.method=="POST":
        student_phone = request.POST.get("number")
        student_balance=request.POST.get("balance")
        list = Student.objects.get(student_phone=student_phone)
        print(list.student_balance)
        if student_balance !='':
            list.student_balance=student_balance
            list.save()
        return render(request, 'manager/charge.html', {'list': list})
    return render(request,'manager/charge.html')
from django.shortcuts import render
from .models import Student
# Create your views here.
def ADD(request):
    if request.method=="POST":
        student_name=request.POST.get("name")
        student_phone=request.POST.get("number")
        student_balance=request.POST.get("balance")
        date=Student(student_name=student_name,student_phone=student_phone,student_balance=student_balance)
        date.save()
    return render(request,'manager/addstudent.html')
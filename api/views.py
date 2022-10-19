from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from manager.models import Student
from random import randint
from .serializer import StudentSerializer
# Create your views here.

@api_view(["GET"])
def GetStudent(request):
    db=Student.objects.all()
    serializer=StudentSerializer(db,many=True)
    return Response(serializer.data)

@api_view(['PUT'])
def PutActivation(request,number):
    db=Student.objects.get(student_phone=number)
    serializer=StudentSerializer(db,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)

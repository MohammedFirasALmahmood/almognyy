from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from manager.models import Student
from .serializer import StudentSerializer
# Create your views here.

@api_view(["GET"])
def GetStudent(request):
    db=Student.objects.all()
    serializer=StudentSerializer(db,many=True)
    return Response(serializer.data)


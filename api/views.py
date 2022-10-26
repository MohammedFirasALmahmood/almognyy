from rest_framework import status
from rest_framework import generics, mixins
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from firstyear.models import AGrammar4M
from firstyear.models import AGrammer1
from firstyear.models import WGrammar
from firstyear.models import AGrammer4
from manager.models import Student
from .serializer import AGrammar1Serializer
from .serializer import AGrammar4MSerializer
from .serializer import StudentSerializer
from .serializer import WGrammarSerializer
from .serializer import AGrammar4Serializer


# Create your views here.

@api_view(['PUT'])
def PutActivation(request, student_phone):
    db = Student.objects.get(student_phone=student_phone)
    if request.method == 'PUT':
        serializer = StudentSerializer(db, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


class GetStudents(APIView):
    def get(self, request):
        db = Student.objects.all()
        serializer = StudentSerializer(db, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class GetStudent(APIView):
    def get_object(self, student_phone):
        try:
            return Student.objects.get(student_phone=student_phone)
        except Student.DoesNotExists:
            raise Http404

    def get(self, request, student_phone):
        db = self.get_object(student_phone)
        serializer = StudentSerializer(db)
        return Response(serializer.data)

    def put(self, request, student_phone):
        db = self.get_object(student_phone)
        serializer = StudentSerializer(db, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class mixins_number(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    def get(self, request, student_phone):
        return self.retrieve(request)

    def put(self, request, student_phone):
        return self.update(request)


class mixins_WGrammar(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = WGrammar.objects.all()
    serializer_class = WGrammarSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class mixins_AGrammer1(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, ):
    queryset = AGrammer1.objects.all()
    serializer_class = AGrammar1Serializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


class mixins_AGrammar4M(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView, ):
    queryset = AGrammar4M.objects.all()
    serializer_class = AGrammar4MSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
@api_view(["GET"])
def GetQuestions(request, ExNo):
    db = AGrammer4.objects.filter(ExNo=ExNo)
    if request.method == 'GET':
        serializer = AGrammar4Serializer(db,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

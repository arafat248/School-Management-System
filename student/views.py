from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Parent, Student
from .serializer import ParentSreializer, StudentSerializer

class ParentViewSet(ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSreializer

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
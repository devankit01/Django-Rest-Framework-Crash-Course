from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .serializers import *
from .models import *

# Permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication


class InstructorListView(generics.ListCreateAPIView):
    queryset =  Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Instructor.objects.all()
    serializer_class = InstructorSerializer

class CourseListView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication] # Auth
    permission_classes = [IsAuthenticated] # Add Permission
    queryset =  Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Course.objects.all()
    serializer_class = CourseSerializer


# URL :  https://www.youtube.com/watch?v=w3PdWkjvUuE&list=PLdBwVRHjcI_845VqggPzu4up0I33o-YO2&index=35
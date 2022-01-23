from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .serializers import *
from .models import *

# Permissions
# from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission
# from rest_framework.authentication import BasicAuthentication, TokenAuthentication

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission

from rest_framework.authtoken.models import Token


# Admin Permission
class WriteByAdmin(BasePermission):
    def has_permission(self,request, view):
        print(request.user)

        user = request.user
        if request.method == "GET":
            return True
        else:
            if user.is_superuser:
                return True
            else:
                False

class InstructorListView(generics.ListCreateAPIView):
    queryset =  Instructor.objects.all()
    serializer_class = InstructorSerializer

class InstructorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Instructor.objects.all()
    serializer_class = InstructorSerializer

class CourseListView(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated,WriteByAdmin]
    queryset =  Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset =  Course.objects.all()
    serializer_class = CourseSerializer


# URL :  https://www.youtube.com/watch?v=w3PdWkjvUuE&list=PLdBwVRHjcI_845VqggPzu4up0I33o-YO2&index=35
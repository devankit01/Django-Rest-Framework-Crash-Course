import stat
from django.shortcuts import render
from rest_framework import status
# Create your views here.
from rest_framework.response import Response

from .models import *
from .serializers import *
from django.http import Http404


# Mixins


# ViewSets
from rest_framework.viewsets import ViewSet, ModelViewSet


# For ModelViewSet
class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



# ViewSet Approach May be contain many Models
'''
class CourseViewSet(ViewSet):
    def list(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CourseSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def retrieve(self, request,pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def destroy(self, request,pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response({"message" : "Deleted"})

    def update(self, request,pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


    pass
'''

'''
# Generics Method

from rest_framework import mixins, generics

# ListCreateAPIView
# class CourseListView(generics.ListAPIView, generics.CreateAPIView):
class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# class CourseDetailView(generics.RetrieveAPIView, generics.UpdateAPIView,generics.DestroyAPIView):
class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
'''


'''
# Mixins Have Actions : list(), create(), retrieve(), update(), delete()
# Generics Have Methods : get(), post(), put(), delete()

class CourseListView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    

class CourseDetailView( generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)

    def delete(self, request, pk):
        return self.destroy(request, pk)

    def put(self, request, pk):
        return self.update(request, pk)

'''



'''

# API View
from rest_framework.views import APIView


class CourseListView(APIView):
    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class CourseDetailView(APIView):
    def get_course(self, id):
        try:
            return Course.objects.get(id=id)
        except:
            raise Http404

    def get(self, request, id):
        serializer = CourseSerializer(self.get_course(id))
        return Response(serializer.data)

    def delete(self, request, id):
        self.get_course(id).delete()
        return Response(status=status.HTTP_204_N0_CONTENT)

    def put(self, request, id):
        course = self.get_course(id)
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
'''

from .models import *
from rest_framework import serializers



# class CourseSerializer(serializers.ModelSerializer):
class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

# class InstructorSerializer(serializers.ModelSerializer):
class InstructorSerializer(serializers.HyperlinkedModelSerializer):
    # courses = CourseSerializer(many = True, read_only = True)
    courses = serializers.HyperlinkedRelatedField(many = True, read_only = True,view_name = 'course-detail')

    class Meta:
        model = Instructor
        fields = '__all__'

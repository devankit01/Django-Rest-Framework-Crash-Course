
from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter
from DRFShort.views import *


router = DefaultRouter()
router.register('courses' , CourseViewSet,  basename = 'course')

from DRFNested.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',include('DRFShort.urls')),
    path('api/',include(router.urls)),

    # Nested Route
    path('ns/api/',InstructorListView.as_view()),
    path('ns/api/<pk>/',InstructorDetailView.as_view(),name="instructor-detail"),
    path('courses/api/',CourseListView.as_view()),
    path('courses/api/<pk>/',CourseDetailView.as_view(),name="course-detail"),


]


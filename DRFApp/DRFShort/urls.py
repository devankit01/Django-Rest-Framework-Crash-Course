from django.urls import path,include
from .views import *


from rest_framework.authtoken import views 
urlpatterns = [
    path('courses/', CourseListView.as_view()),
    path('courses/<pk>/', CourseDetailView.as_view())

 

]

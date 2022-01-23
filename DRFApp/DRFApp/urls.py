
from django.contrib import admin
from django.urls import path,include

from rest_framework.routers import DefaultRouter
from DRFShort.views import *

from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register('courses' , CourseViewSet,  basename = 'course')

from DRFNested.views import *

# JWT Token
from rest_framework_simplejwt.views import (
TokenObtainPairView,
TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',include('DRFShort.urls')),
    path('api/',include(router.urls)),

    # Nested Route
    path('ns/api/',InstructorListView.as_view()),
    path('ns/api/<pk>/',InstructorDetailView.as_view(),name="instructor-detail"),
    path('ns/courses/api/',CourseListView.as_view()),
    path('ns/courses/api/<pk>/',CourseDetailView.as_view(),name="course-detail"),
    path('ns/auth/login/',obtain_auth_token,name="create-token"),

    # JWT Token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]

# Note : Use Bearer_JWTToken for sending auth Request
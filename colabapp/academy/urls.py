from django.urls import path, include
from . import views
from .views import v_course_detail

urlpatterns = [
    path('course', v_course_detail),
]
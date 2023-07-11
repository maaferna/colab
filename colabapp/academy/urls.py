from django.urls import path
from .views import v_course

urlpatterns = [
    path('course', v_course)
]
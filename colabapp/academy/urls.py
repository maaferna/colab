from django.urls import path, include
from . import views
from .views import *


urlpatterns = [
    path('course/<int:course_id>', v_course_detail),
    path('course/<int:course_id>/subscribe', v_subscribe),
]
from django.shortcuts import render
from .models import *
# Create your views here.

def v_index(request):
    context = {
        'course1': Course.objects.get(name = "Matematica Avanzada"),
        'course2': Course.objects.get(name = "Literatura")
    }
    return render(request, 'index.html', context)

def v_course_detail(request, course_id):
    context = {
        'course': Course.objects.get(id = course_id)
    }
    return render(request, 'course.html', context)

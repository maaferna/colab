from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
# Create your views here.
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages

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


@login_required(login_url="/admin/login")
@permission_required("academy.add_subcription", login_url="/admin/login")
def v_subscribe(request, course_id):
    subject = Subject.objects.filter(course_id = course_id).last()
    if subject is None:
        messages.error(request, "No puedes subscribirte en este curso.")
        return HttpResponseRedirect("/academy/course/%s" % (course_id))
    verificar = Subcription.objects.filter(subject_id = subject.id, student_id = request.user.id)
    if verificar.exists():
        messages.success(request, "Tu subscription esta activada.")
        return HttpResponseRedirect("/academy/course/%s" % (course_id))
    else:
        subs = Subcription()
        subs.student_id = request.user.id
        subs.subject_id = subject.id
        subs.save()
        messages.success(request, "Tu subscription fue ingresada de manera correcta.")
        return HttpResponseRedirect("/academy/course/%s" % (course_id))

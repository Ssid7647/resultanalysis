from django.shortcuts import render
from .models import *
from django.http import Http404


def index(request):
    all_students = student_info.objects.all()
    return render(request, 'index.html', {'all_student':all_students} )


def detail(request, studentkey_id):
    try:
        student = resultinfo.objects.get(pk=studentkey_id)
    except resultinfo.DoesNotExist:
        raise Http404(" Information doesn't exist ")
    return render(request, 'detail.html', {'students': student})
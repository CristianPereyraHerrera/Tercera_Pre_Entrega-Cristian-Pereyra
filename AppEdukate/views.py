from django.shortcuts import render
from AppEdukate.models import Course



def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "AppEdukate/about.html")


def course(request):
    return render(request, "AppEdukate/course.html")


def courses(request):
    all_courses = Course.objects.all()
    context = {
        "cursos": all_courses
    }
    return render(request, "AppEdukate/courses.html", context=context)


def students(request):
    return render(request, "index.html")


def teachers(request):
    return render(request, "index.html")

from django.shortcuts import render
from django.http import HttpResponse
from AppEdukate.models import Course, Student, Teacher, Delivery
from collections import defaultdict
from AppEdukate.forms import Form_courses, Form_students, Form_teachers, Form_delivery



##########################################
#                 MENU                   #
##########################################

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "AppEdukate/about.html")


def detail(request):
    return render(request, "AppEdukate/detail.html")


def feature(request):
    return render(request, "AppEdukate/feature.html")


def team(request):
    return render(request, "AppEdukate/team.html")


def testimonial(request):
    return render(request, "AppEdukate/testimonial.html")


def contact(request):
    return render(request, "AppEdukate/contact.html")


##########################################
#                SEARCH                  #
##########################################


def searches(request):
    return render(request, "AppEdukate/searches.html")


def search_courses(request):
    return render(request, "AppEdukate/search_courses.html")


def courses(request):
    name = request.GET.get('name')
    commission = request.GET.get('commission')
    if not name and not commission:
        answer = "You did not enter data"
        return HttpResponse(answer)
    courses = Course.objects.all()
    if name:
        courses = courses.filter(name=name)
    if commission:
        courses = courses.filter(commission=commission)
    if courses.exists():
        return render(request, "AppEdukate/results_search_courses.html", {'courses': courses, 'commission': commission})
    else:
        answer = "No results found"
        return HttpResponse(answer)


def search_students(request):
    return render(request, "AppEdukate/search_students.html")


def students(request):
    name = request.GET.get('name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    if not name and not last_name and not email:
        answer = "You did not enter data"
        return HttpResponse(answer)
    students = Student.objects.all()
    if name:
        students = students.filter(name=name)
    if last_name:
        students = students.filter(last_name=last_name)
    if email:
        students = students.filter(email=email)
    if students.exists():
        return render(request, "AppEdukate/results_search_students.html", {'students': students, 'last_name': last_name,
                                                                           'email': email})
    else:
        answer = "No results found"
        return HttpResponse(answer)


def search_teachers(request):
    return render(request, "AppEdukate/search_teachers.html")


def teachers(request):
    name = request.GET.get('name')
    last_name = request.GET.get('last_name')
    email = request.GET.get('email')
    profession = request.GET.get('profession')
    if not name and not last_name and not email and not profession:
        answer = "You did not enter data"
        return HttpResponse(answer)
    teachers = Teacher.objects.all()
    if name:
        teachers = teachers.filter(name=name)
    if last_name:
        teachers = teachers.filter(last_name=last_name)
    if email:
        teachers = teachers.filter(email=email)
    if profession:
        teachers = teachers.filter(profession=profession)
    if teachers.exists():
        return render(request, "AppEdukate/results_search_teachers.html", {'teachers': teachers, 'last_name': last_name,
                                                                           'email': email, 'profession': profession})
    else:
        answer = "No results found"
        return HttpResponse(answer)


##########################################
#                 FORMS                  #
##########################################


def form_courses(request):
    if request.method == 'POST':
        my_form = Form_courses(request.POST)
        print(my_form)
        if my_form.is_valid:
            information = my_form.cleaned_data
            course = Course(name=information['course'], commission=int(information['commission']))
            course.save()
            return render(request, "AppEdukate/save_form_courses.html")
    else:
        my_form = Form_courses()
    return render(request, "AppEdukate/form_courses.html", {"my_form": my_form})


def form_students(request):
    if request.method == 'POST':
        my_form = Form_students(request.POST)
        print(my_form)
        if my_form.is_valid:
            information = my_form.cleaned_data
            student = Student(name=information['name'], last_name=information['last_name'], email=information['email'])
            student.save()
            return render(request, "AppEdukate/save_form_students.html")
    else:
        my_form = Form_students()
    return render(request, "AppEdukate/form_students.html", {"my_form": my_form})


def form_teachers(request):
    if request.method == 'POST':
        my_form = Form_teachers(request.POST)
        print(my_form)
        if my_form.is_valid:
            information = my_form.cleaned_data
            teacher = Teacher(name=information['name'], last_name=information['last_name'], email=information['email'],
                              profession=information['profession'])
            teacher.save()
            return render(request, "AppEdukate/save_form_teachers.html")
    else:
        my_form = Form_students()
    return render(request, "AppEdukate/form_teachers.html", {"my_form": my_form})


def form_delivery(request):
    if request.method == 'POST':
        my_form = Form_delivery(request.POST)
        print(my_form)
        if my_form.is_valid:
            information = my_form.cleaned_data
            deliveries = Delivery(name=information['name'], last_name=information['last_name'],
                                  course=information['course'], commission=int(information['commission']),
                                  delivery_date=information['delivery_date'], delivered=bool(information['delivered']))
            deliveries.save()
            return render(request, "AppEdukate/save_form_delivery.html")
    else:
        my_form = Form_delivery()
    return render(request, "AppEdukate/form_delivery.html", {"my_form": my_form})


##########################################
#            COURSES AVAIBLES            #
##########################################


def courses_avaibles(request):
    all_courses = Course.objects.all()
    course_counts = defaultdict(int)
    for course in all_courses:
        course_counts[course.name] += 1
    unique_courses = []
    for course_name, count in course_counts.items():
        unique_courses.append({
            "name": course_name,
            "count": count
        })
    context = {
        "courses": unique_courses
    }
    return render(request, "AppEdukate/courses.html", context=context)

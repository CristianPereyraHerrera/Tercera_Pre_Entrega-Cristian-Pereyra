from django.urls import path
from django.views.generic import TemplateView
from AppEdukate.views import courses, students, teachers


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('about/', TemplateView.as_view(template_name='AppEdukate/about.html'), name='about'),
    path('course/', TemplateView.as_view(template_name='AppEdukate/courses.html'), name='course'),
    path('detail/', TemplateView.as_view(template_name='AppEdukate/detail.html'), name='detail'),
    path('feature/', TemplateView.as_view(template_name='AppEdukate/feature.html'), name='feature'),
    path('team/', TemplateView.as_view(template_name='AppEdukate/team.html'), name='team'),
    path('testimonial/', TemplateView.as_view(template_name='AppEdukate/testimonial.html'), name='testimonial'),
    path('contact/', TemplateView.as_view(template_name='AppEdukate/contact.html'), name='contact'),

    path('search_courses/', TemplateView.as_view(template_name='AppEdukate/search_courses.html'), name='search_courses'),
    path('search_students/', TemplateView.as_view(template_name='AppEdukate/search_students.html'), name='search_students'),
    path('search_teachers/', TemplateView.as_view(template_name='AppEdukate/search_teachers.html'), name='search_teachers'),

    path('form_courses/', TemplateView.as_view(template_name='AppEdukate/form_courses.html'), name='form_courses'),
    path('form_students/', TemplateView.as_view(template_name='AppEdukate/form_students.html'), name='form_students'),
    path('form_teachers/', TemplateView.as_view(template_name='AppEdukate/form_teachers.html'), name='form_teachers'),

    path('courses', courses, name="AppEdukateCourses"),
    path('students', students, name="AppEdukateStudents"),
    path('teachers', teachers, name="AppEdukateTeachers"),

]



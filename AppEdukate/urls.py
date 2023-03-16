from django.urls import path
from django.views.generic import TemplateView
from AppEdukate.views import courses, students, teachers


urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='/index'),
    path('about/', TemplateView.as_view(template_name='AppEdukate/about.html'), name='/about'),
    path('course/', TemplateView.as_view(template_name='AppEdukate/course.html'), name='/course'),
    path('detail/', TemplateView.as_view(template_name='AppEdukate/detail.html'), name='/detail'),
    path('feature/', TemplateView.as_view(template_name='AppEdukate/feature.html'), name='/feature'),
    path('team/', TemplateView.as_view(template_name='AppEdukate/team.html'), name='/team'),
    path('testimonial/', TemplateView.as_view(template_name='AppEdukate/testimonial.html'), name='/testimonial'),
    path('contact/', TemplateView.as_view(template_name='AppEdukate/contact.html'), name='/contact'),
    path('courses', courses, name="AppEdukateCourses"),
    path('students', students, name="AppEdukateStudents"),
    path('teachers', teachers, name="AppEdukateTeachers"),
]

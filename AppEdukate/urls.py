from django.urls import path
from AppEdukate.views import courses, students, teachers
from AppEdukate.views import index

urlpatterns = [
    path('', index, name="AppEdukateIndex"),
    path('courses', courses, name="AppEdukateCourses"),
    path('students', students, name="AppEdukateStudents"),
    path('teachers', teachers, name="AppEdukateTeachers"),
]

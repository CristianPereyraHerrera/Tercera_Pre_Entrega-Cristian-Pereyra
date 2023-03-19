from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=30)
    commission = models.IntegerField(unique=True)

    def __str__(self):
        return f"Course: {self.name} ----- Commission: {self.commission}"


class Assignment(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    commission = models.IntegerField()
    assignment_date = models.DateField()
    assignment = models.BooleanField()

    def __str__(self):
        return f"Assignment: {self.name} {self.last_name} ----- Course: {self.course} ----- Commission: {self.commission}" \
               f" ----- Assignment the day: {self.assignment_date} ----- Assignment: {self.assignment}"


class Student(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Student: {self.name} {self.last_name} ----- Email: {self.email}"


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    profession = models.CharField(max_length=30)

    def __str__(self):
        return f"Teacher: {self.name} {self.last_name} ----- Email: {self.email} ----- Profession: {self.profession}"

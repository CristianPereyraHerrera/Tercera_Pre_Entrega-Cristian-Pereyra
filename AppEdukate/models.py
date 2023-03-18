from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=30)
    commission = models.IntegerField(unique=True)

    def __str__(self):
        return f"Course: {self.name} ----- Commission: {self.commission}"


class Delivery(models.Model):
    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    course = models.CharField(max_length=30)
    commission = models.IntegerField(unique=True)
    delivery_date = models.DateField()
    delivered = models.BooleanField()

    def __str__(self):
        return f"Delivery: {self.name} {self.last_name} ----- Course: {self.course} ----- Commission: {self.commission}" \
               f" ----- Delyvered the day: {self.delivery_date} ----- Delyvery: {self.delivered}"


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

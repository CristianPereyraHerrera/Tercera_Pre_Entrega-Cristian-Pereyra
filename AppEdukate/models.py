from django.db import models


class Index(models.Model):
    logo = models.Index


class Course(models.Model):
    name = models.CharField(max_length=30)
    commission = models.IntegerField(unique=True)

    def __str__(self):
        return f"Curso: {self.name} {self.commission}"


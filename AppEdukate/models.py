from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=30)
    commission = models.IntegerField(unique=True)

    def __str__(self):
        return f"Curso: {self.name} {self.commission}"

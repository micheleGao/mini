from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100)
    quote = models.CharField(max_length=100)
    nationality= models.CharField(max_length=100)
    photo_url = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='project')
    title = models.CharField(max_length=100)
    preview_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.title




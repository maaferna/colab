from django.db import models

# Create your models here.

class Teacher(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    bio = models.CharField(max_length=500)

    def __str__(self):
        return self.first_name + self.last_name


class Course(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.name
    
class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT)
    start_date = models.DateField()
    def __str__(self):
        return self.course

class Student(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()
    
    def __str__(self):
        return self.first_name + self.last_name

class Subcription(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.PROTECT)
    student = models.ForeignKey(Student, on_delete=models.PROTECT)
    
    def __str__(self):
        return self.subject + self.student
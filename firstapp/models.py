from django.db import models

# Create your models here.

class Student(models.Model):
    fName = models.CharField(max_length=64)
    rollNo = models.IntegerField(unique=True)
    def __str__(self):
        return f"{self.fName}, {self.rollNo} "

class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="result")
    firstSem = models.IntegerField()
    secondSem = models.IntegerField()
    thirdSem = models.IntegerField()
    aggregate = models.IntegerField(null=True)
    def __str__(self):
        return f"{self.firstSem}, {self.secondSem}, {self.thirdSem}. Aggregate = {self.aggregate}"
    
class User(models.Model):
    username = models.CharField(max_length=64, unique=True)
    password = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.username}, {self.password}"

# CHANGE MODEL INTO SQL (MIGRATIONS)
''' python manage.py makemigrations '''

# LOOK ALL SQL QUERY IS WRITTEN AUTOMATICALLY BY DJANGO
''' python manage.py sqlmigrate firstapp 0001 '''

# APPLYING MIGRATION OR MAKE TABLE TO DB
''' python manage.py migrate '''
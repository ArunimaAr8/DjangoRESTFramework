from django.db import models

# To create tables "class student(inherited class)

class student(models.Model):
    student_id = models.CharField(max_length=20,primary_key=True)
    name = models.CharField(max_length=50)
    mobile = models.IntegerField()


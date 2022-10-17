from django.db import models

# Create your models here.

YEAR_CHOICES = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
)


class Student(models.Model):
    student_name=models.CharField(max_length=500,null=False)
    student_phone=models.CharField(max_length=500,unique=True,null=False)
    student_balance=models.IntegerField(default=0)
    activation_code=models.IntegerField(default=0)


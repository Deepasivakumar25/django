from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    username = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField(
        validators=[
            MinValueValidator(1, message='Age must be a positive integer.'),
            MaxValueValidator(150, message='Age must be less than or equal to 150.')
        ]
    )
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.username
from django.db import models
from django.db.models import CharField, IntegerField


# Create your models here.


class Students (models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()
    contact = models.IntegerField()


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    speed = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.car_name} (Speed: {self.speed} km/h)"


class FormName(models.Model):
    objects = None
    name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=15)
    image = models.ImageField(upload_to="form")

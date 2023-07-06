from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=10)
    # reservation_set 자동생성

class Patient(models.Model):
    name = models.CharField(max_length=10)
    # reservation_set 자동생성
    # 둘다 reservation 에 대한 접근방식만 존재
    doctors = models.ManyToManyField(
        Doctor,
        through='Reservation',
        related_name= 'patients',
    )

class Reservation(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
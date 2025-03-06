from django.contrib.auth.models import AbstractUser
from django.db import models

from django import forms


class User(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True, default=None)
    ID_number = models.CharField(max_length=10, null=True, blank=True, default="")
    driving_licence_number = models.CharField(max_length=10, null=True, blank=True, default="")

    def __str__(self):
        return f"UserName: {self.username} | {self.first_name} {self.last_name} | ID: {self.ID_number} | Date Of Birth: {self.date_of_birth} | DL: {self.driving_licence_number} | email: {self.email}"


class Car(models.Model):
    license_plate = models.CharField(max_length=10)
    vin = models.CharField(max_length=16)
    year = models.CharField(max_length=4)
    brand = models.CharField(max_length=50)
    serie = models.CharField(max_length=70)

    def __str__(self):
        return f"{self.brand} {self.serie} made on {self.year} License Plate: {self.license_plate} , VIN: {self.vin}"


class Insurance(models.Model):
    cost = models.FloatField(default=0)
    coverage_fire = models.BooleanField(default=False)
    coverage_theft = models.BooleanField(default=False)
    coverage_natural_disaster = models.BooleanField(default=False)
    no_clame_discount = models.CharField(max_length=10)
    insured = models.ForeignKey(Car, on_delete=models.CASCADE, blank=False, null=False, related_name="insured")
    policyholder = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False, related_name="policyholder")

    def __str__(self):
        return f"Insurance contract for {self.policyholder.username} covers ${self.cost} for car {self.insured.serie} plate {self.insured.license_plate}, fire: {self.coverage_fire}, theft: {self.coverage_theft}, natural disaster: {self.coverage_natural_disaster}, discount: {self.no_clame_discount}"


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to ='media/')
    date_of_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}: {self.content}"

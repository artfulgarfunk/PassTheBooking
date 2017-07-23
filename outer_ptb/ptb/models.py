from django.db import models
from django.forms import ModelForm
from django.utils.translation import gettext as _

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

class Property(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    pet_friendly = models.BooleanField(blank=False)
    bathrooms = models.PositiveIntegerField(blank=False)
    bedrooms = models.PositiveIntegerField(blank=False)

    def __str__(self):
        return self.address

class Booking(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=False)
    date_from = models.DateField(blank=False)
    date_until = models.DateField(blank=False)

    def __str__(self):
        return self.first_name

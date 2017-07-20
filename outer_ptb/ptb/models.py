from django.db import models

# Create your models here.
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    # add in phone number

    #  what is the point of this method? why in tutorial
    def __str__(self):
        return self.first_name

class Property(models.Model):
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.address

class Booking(models.Model):
    prop = models.ForeignKey(Property, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(blank=False)
    date_from = models.DateTimeField(blank=False)
    date_until = models.DateTimeField(blank=False)

    def __str__(self):
        return self.first_name

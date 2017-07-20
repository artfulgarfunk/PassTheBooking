from django.contrib import admin

from .models import Client
from .models import Property
from .models import Booking

admin.site.register(Client)
admin.site.register(Property)
admin.site.register(Booking)

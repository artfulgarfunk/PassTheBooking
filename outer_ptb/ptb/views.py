from django.shortcuts import render, redirect
# FORMS
from .forms import ClientForm
from .forms import PropertyForm
from .forms import BookingForm

# MODELS
from .models import Client
from .models import Property
from .models import Booking

def home(request):
    return render(request, 'ptb/home.html', {} )

def clients(request):
    clients = Client.objects.order_by('first_name')
    return render(request, 'ptb/client_index.html', {'clients': clients} )

def client_info(request, num):
    client = Client.objects.get(id=num)
    return render(request, 'ptb/client.html', { 'client': client } )

def client_properties(request, num):
    client = Client.objects.get(id=num)
    properties = Property.objects.filter(owner=client)
    return render(request, 'ptb/client_properties.html', { 'properties': properties, 'client': client})

def client_edit(request, num):
    instance = Client.objects.get(id=num)
    edit = False
    form = ClientForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        edit = True
    return render(request, 'ptb/client_edit.html', {'form':form, 'edit': edit,'client':instance})


def property_index(request):
    properties = Property.objects.all()
    return render(request, 'ptb/property_index.html', { 'properties': properties })

def property_info(request, num):
    prop = Property.objects.get(id=num)
    bookings = Booking.objects.filter(prop=prop)
    return render(request, 'ptb/property.html', { 'property': prop, 'bookings': bookings } )

def property_edit(request, num):
    instance = Property.objects.get(id=num)
    edit = False
    form = PropertyForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        edit = True
    return render(request, 'ptb/property_edit.html', {'form':form, 'edit': edit, 'property': instance })

def booking_info(request, num):
    booking = Booking.objects.get(id=num)
    return render(request, 'ptb/booking.html', { 'booking': booking})

def booking_index(request):
    bookings = Booking.objects.all()
    return render(request, 'ptb/booking_index.html', { 'bookings': bookings })

def booking_edit(request,num):
    instance = Booking.objects.get(id=num)
    edit = False
    form = BookingForm(request.POST or None, instance=instance)
    if form.is_valid():
        form.save()
        edit = True
    return render(request, 'ptb/booking_edit.html', {'form':form, 'edit': edit, 'booking': instance })

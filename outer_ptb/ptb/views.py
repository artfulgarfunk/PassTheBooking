from django.shortcuts import render
from .models import Client
from .models import Property
from .models import Booking
# Create your views here.

def home(request):
    return render(request, 'ptb/home.html', {} )

def clients(request):
    clients = Client.objects.order_by('first_name')
    return render(request, 'ptb/client_index.html', {'clients': clients} )

def client_info(request, num):
    client = Client.objects.get(id=num)
    return render(request, 'ptb/client.html', { 'client': client } )

def client_property(request, num):
    client = Client.objects.get(id=num)
    properties = Property.objects.filter(owner=client)
    return render(request, 'ptb/client_properties.html', { 'properties': properties, 'client': client})

def property_index(request):
    properties = Property.objects.all()
    return render(request, 'ptb/property_index.html', { 'properties': properties })

def property_info(request, num):
    prop = Property.objects.get(id=num)
    return render(request, 'ptb/property.html', { 'property': prop } )

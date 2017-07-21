from django.shortcuts import render
from .models import Client
from .models import Property
from .models import Booking
# Create your views here.

def home(request):
    return render(request, 'ptb/home.html', {} )

def clients(request):
    clients = Client.objects.order_by('first_name')
    return render(request, 'ptb/clients.html', {'clients': clients} )

def client_info(request, num):
    client = Client.objects.get(id=num)
    return render(request, 'ptb/client.html', { 'client': client } )

from django.shortcuts import render
from .models import Client
from .models import Property
from .models import Booking
# Create your views here.

def home(request):
    return render(request, 'ptb/home.html', {} )

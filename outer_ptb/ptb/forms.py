from django import forms
from .models import Client
from .models import Property
from .models import Booking

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = ('first_name', 'last_name', 'email',)

class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('address', 'pet_friendly','bathrooms','bedrooms')

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('first_name', 'last_name', 'email','date_from','date_until')

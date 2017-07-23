from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'clients/$', views.clients, name='client_index'),
    url(r'^clients/(?P<num>[0-9]+)/$', views.client_info, name='client_info'),
    url(r'^clients/(?P<num>[0-9]+)/properties/$', views.client_properties, name='properties'),
    url(r'^properties/$', views.property_index, name='property_index'),
    url(r'^properties/(?P<num>[0-9]+)/$', views.property_info, name='property_info'),
    url(r'^properties/(?P<num>[0-9]+)/edit/$', views.property_edit, name='property_edit'),
    url(r'^clients/(?P<num>[0-9]+)/edit/$', views.client_edit, name='client_edit'),
    url(r'^bookings/(?P<num>[0-9]+)/$', views.booking_info, name='booking_info'),
    url(r'^bookings/$', views.booking_index, name='booking_index'),
    url(r'^bookings/(?P<num>[0-9]+)/edit/$', views.booking_edit, name='booking_edit'),

]

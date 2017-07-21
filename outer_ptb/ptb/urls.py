from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'clients/$', views.clients, name='client_index'),
    url(r'^clients/(?P<num>[0-9]+)/$', views.client_info, name='client_info'),
    url(r'^clients/(?P<num>[0-9]+)/properties/$', views.client_property, name='properties'),
    url(r'^properties/$', views.property_index, name='property_index'),
    url(r'^properties/(?P<num>[0-9]+)/$', views.property_info, name='property_info'),


]

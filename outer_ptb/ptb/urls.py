from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'clients/$', views.clients, name='index'),
    url(r'^clients/(?P<num>[0-9]+)/$', views.client_info, name='client_info'),

]

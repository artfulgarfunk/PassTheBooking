from django.test import TestCase
from ptb.models import Client
from ptb.models import Property
from ptb.models import Booking


class ptbViewsTestCase(TestCase):
    def test_index(self):
        response = self.client.get('/ptb/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/home.html')
        self.assertContains(response, '<h1> Pass The Booking </h1>')

    def test_clients(self):
        response = self.client.get('/ptb/clients/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/clients.html')
        self.assertContains(response, '<h1> Clients </h1>')


class ptbClientModelTestCase(TestCase):

    def create_client(self, first_name="jack", last_name="henderson", email="jack@email.com"):
        return Client.objects.create(first_name = first_name, last_name = last_name, email = email)

    def test_client_creation(self):
        c = self.create_client()
        self.assertTrue(isinstance(c, Client))
        self.assertEqual(c.__str__(), c.first_name)

class ptbPropertyModelTestCase(TestCase):

    def create_property(self,address="street"):
        c = ptbClientModelTestCase().create_client()
        return Property.objects.create(owner=c,address=address)

    def test_property_creation(self):
        p = self.create_property()
        self.assertTrue(isinstance(p, Property))
        self.assertEqual(p.__str__(), p.address)


class ptbBookingModelTestCase(TestCase):

    def create_booking(self, first_name="jim", last_name="morrison", email="jim@email.com", date_from = "2014-12-08T15:43:00", date_until = "2014-12-08T15:43:00"):
        p = ptbPropertyModelTestCase().create_property()
        return Booking.objects.create(prop=p, first_name = first_name, last_name = last_name, email = email, date_from = date_from, date_until = date_until)

    def test_booking_creation(self):
        b = self.create_booking()
        self.assertTrue(isinstance(b, Booking))
        self.assertEqual(b.__str__(), b.first_name)

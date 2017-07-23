from django.test import TestCase
from ptb.models import Client, Property, Booking
from ptb.forms import ClientForm, PropertyForm, BookingForm

# TEMPLATE UNIT TESTS
class ptbTemplateFeatureTestCase(TestCase):

    def create_client(self, first_name="jack", last_name="henderson", email="jack@email.com"):
        return Client.objects.create(first_name = first_name, last_name = last_name, email = email)

    def create_property(self,address="street", pet_friendly=True, bathrooms=2, bedrooms=3):
        c = self.create_client()
        return Property.objects.create(owner=c,address=address, pet_friendly = pet_friendly, bathrooms=bathrooms, bedrooms=3)

    def create_booking(self, first_name="jim", last_name="morrison", email="jim@email.com", date_from = "2014-12-08", date_until = "2016-12-08"):
        p = self.create_property()
        return Booking.objects.create(prop=p, first_name = first_name, last_name = last_name, email = email, date_from = date_from, date_until = date_until)

    def test_clients_index(self):
        c = self.create_client()
        response = self.client.get('/ptb/clients/')
        self.assertContains(response, c.first_name)
        self.assertContains(response, c.last_name)
        self.assertContains(response, c.email)
        self.assertContains(response, c.id)

    def test_client_info(self):
        c = self.create_client()
        response = self.client.get('/ptb/clients/1/')
        self.assertContains(response, c.first_name)
        self.assertContains(response, c.last_name)
        self.assertContains(response, c.email)
        self.assertContains(response, c.id)
        self.assertContains(response, "Edit")
        self.assertContains(response, "Client Properties")

    def test_client_edit(self):
        c = self.create_client()
        response = self.client.get('/ptb/clients/1/edit/')
        self.assertContains(response, "First name:")
        self.assertContains(response, "Last name:")
        self.assertContains(response, "Email:")
        self.assertContains(response, "Save")

    def test_clients_properties(self):
        p = self.create_property()
        response = self.client.get('/ptb/clients/1/properties/')
        self.assertContains(response, p.owner.first_name)
        self.assertContains(response, p.owner.last_name)
        self.assertContains(response, p.address)
        self.assertContains(response, "Property Details")

    def test_property_index(self):
        p = self.create_property()
        response = self.client.get('/ptb/properties/')
        self.assertContains(response, p.address)
        self.assertContains(response, p.owner.first_name)
        self.assertContains(response, p.owner.last_name)
        self.assertContains(response, "Property Details")
        self.assertContains(response, "Client Details")

    def test_property_info(self):
        p = self.create_property()
        response = self.client.get('/ptb/properties/1/')
        self.assertContains(response, p.address)
        self.assertContains(response, p.bathrooms)
        self.assertContains(response, p.bedrooms)
        self.assertContains(response, "Yes")
        self.assertContains(response, "Edit")
        self.assertContains(response, "Client Details")

    def test_property_edit(self):
        p = self.create_property()
        response = self.client.get('/ptb/properties/1/edit/')
        self.assertContains(response, "Address:")
        self.assertContains(response, "Pet friendly:")
        self.assertContains(response, "Bathrooms:")
        self.assertContains(response, "Bedrooms:")
        self.assertContains(response, "Save")

    def test_booking_index(self):
        b = self.create_booking()
        response = self.client.get('/ptb/bookings/')
        self.assertContains(response, "Bookings")
        self.assertContains(response, b.prop.address)
        self.assertContains(response, "Dec. 8, 2014")
        self.assertContains(response, "Dec. 8, 2016")
        self.assertContains(response, "View Booking")

    def test_booking_info(self):
        b = self.create_booking()
        response = self.client.get('/ptb/bookings/1/')
        self.assertContains(response, b.prop.address)
        self.assertContains(response, b.first_name)
        self.assertContains(response, b.last_name)
        self.assertContains(response, b.email)
        self.assertContains(response, "Edit")
        self.assertContains(response, "View Property")
        self.assertContains(response, "View Client")

    def test_booking_edit(self):
        b = self.create_booking()
        response = self.client.get('/ptb/bookings/1/edit/')
        self.assertContains(response, "First name:")
        self.assertContains(response, "Last name:")
        self.assertContains(response, "Date from:")
        self.assertContains(response, "Date until:")
        self.assertContains(response, "Save")


# VIEW UNIT TESTS
class ptbViewsTestCase(TestCase):
    fixtures = ['data.json']

    def test_home(self):
        response = self.client.get('/ptb/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/home.html')

    def test_clients_index(self):
        response = self.client.get('/ptb/clients/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/client_index.html')

    def test_single_client_info(self):
        response = self.client.get('/ptb/clients/2/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/client.html')

    def test_clients_properties(self):
        response = self.client.get('/ptb/clients/3/properties/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/client_properties.html')

    def test_property_index(self):
        response = self.client.get('/ptb/properties/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/property_index.html')

    def test_single_property_info(self):
        response = self.client.get('/ptb/properties/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/property.html')

    def test_booking_index(self):
        response = self.client.get('/ptb/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/booking_index.html')

    def test_single_booking_info(self):
        response = self.client.get('/ptb/bookings/2/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/booking.html')

class ptbViewsNoData(TestCase):

    def test_clients_properties_no_data(self):
        Client.objects.create(first_name="David",last_name="Bowie",email="bowie@email.com")
        response = self.client.get('/ptb/clients/1/properties/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This client has no properties yet")

    def test_clients_no_data(self):
        response = self.client.get('/ptb/clients/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no clients yet")

    def test_properties_no_data(self):
        response = self.client.get('/ptb/properties/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no properties listed yet")

    def test_bookings_no_data(self):
        response = self.client.get('/ptb/bookings/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no bookings yet")

# MODEL UNIT TESTS
class ptbClientModelTestCase(TestCase):

    def create_client(self, first_name="jack", last_name="henderson", email="jack@email.com"):
        return Client.objects.create(first_name = first_name, last_name = last_name, email = email)

    def test_client_creation(self):
        c = self.create_client()
        self.assertTrue(isinstance(c, Client))
        self.assertEqual(c.__str__(), c.first_name)

class ptbPropertyModelTestCase(TestCase):

    def create_property(self,address="street", pet_friendly=True, bathrooms=2, bedrooms=3):
        c = ptbClientModelTestCase().create_client()
        return Property.objects.create(owner=c,address=address, pet_friendly = pet_friendly, bathrooms=bathrooms, bedrooms=3)

    def test_property_creation(self):
        p = self.create_property()
        self.assertTrue(isinstance(p, Property))
        self.assertEqual(p.__str__(), p.address)


class ptbBookingModelTestCase(TestCase):

    def create_booking(self, first_name="jim", last_name="morrison", email="jim@email.com", date_from = "2014-12-08", date_until = "2014-12-08"):
        p = ptbPropertyModelTestCase().create_property()
        return Booking.objects.create(prop=p, first_name = first_name, last_name = last_name, email = email, date_from = date_from, date_until = date_until)

    def test_booking_creation(self):
        b = self.create_booking()
        self.assertTrue(isinstance(b, Booking))
        self.assertEqual(b.__str__(), b.first_name)

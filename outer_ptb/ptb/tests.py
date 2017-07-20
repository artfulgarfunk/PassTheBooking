from django.test import TestCase


class PollsViewsTestCase(TestCase):
    def test_index(self):
        response = self.client.get('/ptb/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ptb/home.html')
        self.assertContains(response, '<h1> Pass The Booking </h1>')

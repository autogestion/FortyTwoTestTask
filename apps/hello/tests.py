
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client
from .models import Contact


class HttpTest(TestCase):
    def test_home(self):
        myself = Contact.objects.get(id=1)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, myself.first_name)
        self.assertContains(response, myself.last_name)
        self.assertContains(response, myself.skype)

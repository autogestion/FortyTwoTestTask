
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import Client, RequestFactory
from django.conf import settings
from django.template import RequestContext


from .models import Contact, HttpRequestList
from .middleware import SaveAllHttpRequests
from .views import requestList
from .context_processors import load_settings


class ContactTest(TestCase):
    def test_home(self):
        myself = Contact.objects.all()[0]
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, myself.first_name)
        self.assertContains(response, myself.last_name)
        self.assertContains(response, myself.skype)



class MiddlewareTest(TestCase):
     def test_requests_middleware(self):
         self.factory = RequestFactory()
         request = self.factory.get(reverse('requestList'))
         response = requestList(request)
         self.assertEqual(response.status_code, 200)
         md = SaveAllHttpRequests()
         count = HttpRequestList.objects.all().count()
         md.process_request(request)
         self.assertNotEqual(HttpRequestList.objects.all().count(), count)


class TestContext(TestCase):
    def test_load_settings(self):
        factory = RequestFactory()
        request = factory.get('/')
        context = RequestContext(request, None, [load_settings])
        self.assertIn('settings', context)
        self.assertEqual(context['settings'], settings)

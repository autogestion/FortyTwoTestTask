
from django.core.urlresolvers import reverse
from django.test import TestCase
from django.test.client import RequestFactory
from django.conf import settings
from django.contrib.auth import authenticate
from django.template import Template, Context, RequestContext
from django.core.management import get_commands, call_command
from django.db import models
from StringIO import StringIO

from .models import Contact, HttpRequestList, Signal
from .middleware import SaveAllHttpRequests
from .views import requestList
from .context_processors import load_settings



class HttpTest(TestCase):

    fixtures = ("initial_data")

    def test_home(self):
        myself = Contact.objects.all()[0]
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, myself.first_name)
        self.assertContains(response, myself.last_name)
        self.assertContains(response, myself.skype)

    def test_edit_page(self):
        response = self.client.get(reverse('edit_page'))
        self.assertRedirects(response, reverse('login')+'?next=/edit/')

        self.client.login(username='admin', password='admin')
        response = self.client.get(reverse('edit_page'))
        self.assertEqual(response.status_code, 200)
        data = {
            'first_name': "foo",
            'last_name': "bar",
            'birthday': '2012-12-12',
            'bio': 'some bio about me',
            'email': 'g@g.com',
            'jabber': 'g@jabber.org.ua',
            'skype': 'gg',
            'other_contacts': '333'
        }
        response = self.client.post(reverse('edit_page'), data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, data['first_name'])
        self.assertContains(response, data['last_name'])
        self.assertContains(response, data['email'])
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'logout')
        self.assertContains(response, 'edit')
        self.client.get(reverse('logout_user'))
        response = self.client.get(reverse('home'))
        self.assertContains(response, 'login')


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


# class WidgetsTest(TestCase):
#     def test_datepicker(self):
#         JS_SCRIPTS = [
#             'jquery-ui-1.11.0.custom.min.js',
#             'jquery-1.11.1.min.js'
#         ]
#         self.client.login(username='admin', password='admin')
#         response = self.client.post(reverse('edit_page'))
#         self.assertContains(response, 'id_birthday')
#         for script in JS_SCRIPTS:
#             self.assertContains(response, script)



class AdminTagTest(TestCase):
    def test_generate_link(self):
        tag_tpl = '<a href="/admin/auth/user/1/">(admin)</a>'
        user = authenticate(username='admin', password='admin')
        tag = Template('{% load admintag %}{% edit_link user %}') \
                      .render(Context({'user': user}))
        self.assertEqual(tag_tpl, tag)

    def test_tag_exist(self):
        tag_tpl = '<a href="/admin/auth/user/1/">(admin)</a>'
        self.client.login(username="admin", password="admin")
        response = self.client.get(reverse('home'))
        self.assertContains(response, tag_tpl)



class CommandTest(TestCase):
    def test_showmodules(self):
        self.assertTrue('showmodels' in get_commands())
        content = StringIO()
        error = StringIO()
        call_command('showmodels', stdout=content, stderr=error, error=True)
        for model in models.get_models():
            name = str(model).split("'")[1]
            self.assertIn(name, content.getvalue())
            self.assertIn(name, error.getvalue())


class SignalProcessors(TestCase):
    def test_signals(self):
        Contact.objects.create(first_name='Foo', birthday='2012-12-12')
        info = Contact.objects.latest('id')
        info.save()
        info.delete()
        singals = Signal.objects.order_by("-date")[:3]
        singals = list(singals)
        models_singals = [
            ['Contact', 'delete'],
            ['Contact', 'edit'],
            ['Contact', 'create'],
        ]
        self.assertEqual(len(singals), 3)
        for index, value in enumerate(models_singals):
            model, signal = value
            self.assertEqual(singals[index].model, model)
            self.assertEqual(singals[index].signal, signal)

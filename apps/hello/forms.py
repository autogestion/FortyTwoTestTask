
from django.forms import ModelForm
from django.conf import settings
from django import forms

from .models import Contact
from .widgets import Calendar


class info_form(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'birthday', 'bio', 'email',
                  'jabber', 'skype', 'other_contacts', 'photo']
        widgets = {
                    'birthday': Calendar(params="dateFormat: 'yy-mm-dd'"),
                    'photo': forms.FileInput
                    }

    class Media:
        js = (
            settings.STATIC_URL + 'js/form.js',
            settings.STATIC_URL + 'js/jquery.form.js',
            settings.STATIC_URL + 'js/edit_detail.js',
        )

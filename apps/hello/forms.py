from django.forms import ModelForm
from .models import Contact


class info_form(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'birthday', 'bio', 'email',
                  'jabber', 'skype', 'other_contacts', 'photo']

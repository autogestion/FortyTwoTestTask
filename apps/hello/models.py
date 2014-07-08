from django.db import models

class Contact(models.Model):
    first_name = models.CharField(verbose_name="Name", max_length=100)
    last_name = models.CharField(verbose_name="Last name", max_length=100)
    birthday = models.DateField("Birthday")
    bio = models.TextField(verbose_name="Bio")
    email = models.EmailField(verbose_name="Email")
    jabber = models.CharField(verbose_name="Jabber", max_length=100)
    skype = models.CharField(verbose_name="Skype", max_length=100)
    other_contacts = models.TextField(verbose_name="Other contacts")

from django.db import models
from datetime import datetime

class Contact(models.Model):
    first_name = models.CharField(verbose_name="Name", max_length=100)
    last_name = models.CharField(verbose_name="Last name", max_length=100)
    birthday = models.DateField("Birthday")
    bio = models.TextField(verbose_name="Bio")
    email = models.EmailField(verbose_name="Email")
    jabber = models.CharField(verbose_name="Jabber", max_length=100)
    skype = models.CharField(verbose_name="Skype", max_length=100)
    other_contacts = models.TextField(verbose_name="Other contacts")


    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)


class HttpRequestList(models.Model):
    date = models.DateTimeField("Date", default=datetime.now, blank=True)
    method = models.CharField(verbose_name="Method", max_length=50)
    protocol = models.CharField(verbose_name="Protocol", max_length=50)
    remote_addr = models.CharField(verbose_name="Remote addr", max_length=100)
    path_info = models.CharField(verbose_name="Path info", max_length=255)


    def __unicode__(self):
        return "%s %s" %(self.date, self.path_info)

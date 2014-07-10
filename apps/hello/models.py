from django.db import models
from datetime import datetime
from annoying.decorators import signals

class Contact(models.Model):
    first_name = models.CharField(verbose_name="Name", max_length=100)
    last_name = models.CharField(verbose_name="Last name", max_length=100)
    birthday = models.DateField("Birthday")
    bio = models.TextField(verbose_name="Bio")
    email = models.EmailField(verbose_name="Email")
    jabber = models.CharField(verbose_name="Jabber", max_length=100)
    skype = models.CharField(verbose_name="Skype", max_length=100)
    other_contacts = models.TextField(verbose_name="Other contacts")
    photo = models.ImageField(upload_to='photos', blank=True, null=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)





class HttpRequestList(models.Model):
    date = models.DateTimeField("Date", default=datetime.now, blank=True)
    method = models.CharField(verbose_name="Method", max_length=50)
    protocol = models.CharField(verbose_name="Protocol", max_length=50)
    remote_addr = models.CharField(verbose_name="Remote addr", max_length=100)
    path_info = models.CharField(verbose_name="Path info", max_length=255)
    priority = models.PositiveIntegerField(verbose_name="priority", default=1)

    def __unicode__(self):
        return "%s %s" %(self.date, self.path_info)




class Signal(models.Model):
    object_id = models.IntegerField(verbose_name="object id")
    date = models.DateTimeField(verbose_name="date", auto_now_add=True)
    model = models.CharField(verbose_name="model", max_length=50)
    signal = models.CharField(verbose_name="signal", max_length=50)

    def __unicode__(self):
        return unicode('%s - %s' % (self.model, self.signal))


@signals.post_save()
def signals_handler(instance, **kwargs):
    model = instance._meta.object_name
    if model != 'Signal':
        signal = 'create' if kwargs['created'] else 'edit'
        try:
            Signal.objects.create(
                model=model,
                signal=signal,
                object_id=instance.id
            )
        except:
            return


@signals.post_delete()
def delete_handler(instance, **kwargs):
    model = instance._meta.object_name
    if model != 'Signal':
        try:
            Signal.objects.create(
                model=model,
                signal='delete',
                object_id=instance.id
            )
        except:
            return

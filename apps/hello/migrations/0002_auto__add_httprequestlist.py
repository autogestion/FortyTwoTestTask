# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'HttpRequestList'
        db.create_table(u'hello_httprequestlist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, blank=True)),
            ('method', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('protocol', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('remote_addr', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('path_info', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'hello', ['HttpRequestList'])


    def backwards(self, orm):
        # Deleting model 'HttpRequestList'
        db.delete_table(u'hello_httprequestlist')


    models = {
        u'hello.contact': {
            'Meta': {'object_name': 'Contact'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'other_contacts': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'hello.httprequestlist': {
            'Meta': {'object_name': 'HttpRequestList'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'method': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'path_info': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'remote_addr': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['hello']
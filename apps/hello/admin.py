from django.contrib import admin

from .models import Contact, HttpRequestList


admin.site.register(Contact)
admin.site.register(HttpRequestList)

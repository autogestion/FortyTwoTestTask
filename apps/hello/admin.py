from django.contrib import admin

from .models import Contact, HttpRequestList, Signal


admin.site.register(Contact)
admin.site.register(HttpRequestList)
admin.site.register(Signal)

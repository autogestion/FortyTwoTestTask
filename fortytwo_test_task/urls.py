from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login
from django.conf import settings
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^$', 'apps.hello.views.home', name='home'),
    url(r'^requests/$', 'apps.hello.views.requestList', name='requestList'),
    url(r'^edit/$', 'apps.hello.views.edit_page',
        name='edit_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^uploads/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^login/$', login, name="login"),
    url(r'^logout/$', 'apps.hello.views.logout_user',
        name="logout_user"),
)

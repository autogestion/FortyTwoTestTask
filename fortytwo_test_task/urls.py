from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:

    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'apps.hello.views.home', name='home'),
    url(r'^requests/$', 'apps.hello.views.requestList', name='requestList'),
    url(r'^admin/', include(admin.site.urls)),
)

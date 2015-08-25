from django.conf.urls import patterns, include, url
from django.contrib import admin

from journal.views import index as index_func

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^emails/',
        include('django_inbound_email.urls')
    ),
    url(r'^$', index_func),
)

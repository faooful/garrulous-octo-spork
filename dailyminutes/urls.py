from django.conf.urls import patterns, include, url
from django.contrib import admin

from journal.views import index as index_func

from journal.views import receive_email

urlpatterns = patterns(
    '',
    url(r'^receive_email/', receive_email),
    url(r'^admin/', include(admin.site.urls)),
    url(
        r'^emails/',
        include('django_inbound_email.urls')
    ),
    url(r'^$', index_func),
)

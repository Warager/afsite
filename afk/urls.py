from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^$', 'afk.af-kvadr.views.home'),
    url(r'^about$', 'afk.af-kvadr.views.about'),
    url(r'^scope$', 'afk.af-kvadr.views.scope'),
    url(r'^contact$', 'afk.af-kvadr.views.contact'),
    url(r'^zurb$', 'afk.af-kvadr.views.zurb'),

    url(r'^admin/', include(admin.site.urls)),
)

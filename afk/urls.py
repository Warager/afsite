from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^$', 'afc.afcapp.views.home'),
    url(r'^about$', 'afc.afcapp.views.about'),
    url(r'^scope$', 'afc.afcapp.views.scope'),
    url(r'^contact$', 'afc.afcapp.views.contact'),
    url(r'^zurb$', 'afc.afcapp.views.zurb'),

    url(r'^admin/', include(admin.site.urls)),
)

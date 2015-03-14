from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    url(r'^$', 'af2.af2app.views.home'),
    url(r'^about$', 'af2.af2app.views.about'),
    url(r'^scope$', 'af2.af2app.views.scope'),
    url(r'^contact$', 'af2.af2app.views.contact'),
    url(r'^zurb$', 'af2.af2app.views.zurb'),

    url(r'^admin/', include(admin.site.urls)),
)

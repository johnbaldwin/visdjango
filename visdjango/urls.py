from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'visdjango.views.home', name='home'),
    url(r'^intro/', include('intro.urls')),
    url(r'^d3/', include('d3.urls')),
    url(r'^nvd3/', include('nvd3.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

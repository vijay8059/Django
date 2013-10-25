from django.conf.urls import patterns, include, url
from django.contrib import admin
     
admin.autodiscover()
     
urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
         url(r'^$', 'spreadsheet_app.views.index'),
         #url(r'^(?P<slug>[\w\-]+)/$', 'spreadsheet_app.views.post'),
    )
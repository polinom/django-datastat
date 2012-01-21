from django.conf.urls.defaults import patterns, url
from datastat.views import modelstat

urlpatterns = patterns('',
    url(r'^(?P<app_label>[a-zA-Z0-9_-]+)/(?P<model_name>[a-zA-Z0-9_-]+)/$', modelstat , name='chart_url'),
)

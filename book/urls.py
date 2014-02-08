from django.conf.urls import patterns, url
from .views import index, read


urlpatterns = patterns('',
    url(r'index/$', index, name='book'),
    url(r'read/(?P<slug>.+)/$', read, name='read'),
)

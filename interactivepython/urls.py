from django.conf.urls import patterns, include, url
from django.conf import settings
from .views import index
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'interactivepython.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^book/', include('book.urls')),
    url(r'^$', index, name='index'),
    url('^markdown/', include( 'django_markdown.urls')),
)

urlpatterns += staticfiles_urlpatterns()

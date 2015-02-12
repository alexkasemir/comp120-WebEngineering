from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'purrer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^meows/', include('meows.urls', namespace="meows")),

    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'media'}
))
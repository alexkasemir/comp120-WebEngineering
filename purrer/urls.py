from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
# import html5_appcache
# html5_appcache.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'purrer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'', include('meows.urls', namespace="meows")),

    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('', (
        r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': 'media'}
))

# urlpatterns += patterns('',
#     url('^', include('html5_appcache.urls')),
# )


# urlpatterns += patterns('', (
#         r'^media/(?P<path>.*)$',
#         'django.views.static.serve',
#         {'document_root': settings.MEDIA_ROOT}
# )) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.conf.urls import patterns, url, include
from meows import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^tag/(?P<tag>\S+)$', views.hashtag_index),
    url(r'^prefs', views.user_pref),
    url(r'^user/(?P<user>\S+)$', views.user_index),
    url(r'^(?P<user_post_id>\d+)/$', views.detail, name='detail'),
    url(r'^new_post', views.new_post, name='new_post'),
    url(r'^create_post', views.create_post, name='create_post'),
    url(r'^like/(?P<user_post_id>\d+)/$', views.post_like),
    url(r'^dislike/(?P<user_post_id>\d+)/$', views.post_dislike),
    url(r'^api/posts/(?P<user_post_id>\d+)$', views.api_post_element),
    url(r'^api/posts_group/(?P<user_post_id>\d+)$', views.api_post_group),
    url(r'^api/users/(?P<user_id>\d+)$', views.api_user_element),
    url(r'^api/posts', views.api_post_collection),
    url(r'^api/users', views.api_user_collection),
    url(r'^api/docs', views.api_docs),
    url(r'^accounts/register$', views.register),
    url(r'^accounts/register_user', views.register_user),
    url(r'^accounts/login_user$', views.login_user),
    url(r'^accounts/login', views.login),
    url(r'^accounts/logout$', views.logout, name='logout'),
    #url('^', include('django.contrib.auth.urls')),
    #url('^login/', 'django.contrib.auth.views.login', {'template_name': 'meows/Pages/login.html'}),
)

# urlpatterns += patterns('',
#     url('^', include('html5_appcache.urls')),
# )

# urlpatterns += patterns('', (
#         r'^static/(?P<path>.*)$',
#         'django.views.static.serve',
#         {'document_root': 'media'}
# ))
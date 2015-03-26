from django.conf.urls import patterns, url
from meows import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_post_id>\d+)/$', views.detail, name='detail'),
    url(r'^new_post', views.new_post, name='new post'),
    url(r'^create_post', views.create_post, name='create_post'),
    url(r'^like/(?P<user_post_id>\d+)/$', views.post_like),
    url(r'^dislike/(?P<user_post_id>\d+)/$', views.post_dislike),
    url(r'^api/posts/(?P<user_post_id>\d+)$', views.api_post_element),
    url(r'^api/users/(?P<user_id>\d+)$', views.api_user_element),
    url(r'^api/posts', views.api_post_collection),
    url(r'^api/users', views.api_user_collection),
<<<<<<< HEAD
    
=======
    url(r'^api/docs', views.api_docs),
>>>>>>> 8803ecaef4d8b008ddc8de4553fd3407cc52ceec
)

# urlpatterns += patterns('',
#     url('^', include('html5_appcache.urls')),
# )

# urlpatterns += patterns('', (
#         r'^static/(?P<path>.*)$',
#         'django.views.static.serve',
#         {'document_root': 'media'}
# ))
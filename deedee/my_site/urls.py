from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('my_site.views',
    url(r'^index/$', 'index'),
    url(r'^$', 'index'),
    url(r'posts/(?P<post_id>\d+)/$', 'details'),
    url(r'^category/(?P<category_name>\w+)/$', 'category'),
)

urlpatterns += staticfiles_urlpatterns()

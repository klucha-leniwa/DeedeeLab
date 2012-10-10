from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('my_site.views',
    url(r'^index/$', 'index'),
    url(r'^$', 'index'),
    url(r'^base/$', 'base'),
    url(r'posts/(?P<post_id>\d+)/$', 'details'),
    url(r'^category/(?P<category_name>\w+)/$', 'category'),
    url(r'^form/$', 'manage_comment')
)

urlpatterns += staticfiles_urlpatterns()

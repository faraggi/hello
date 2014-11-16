from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'places.views.home', name='home'),
    url(r'^(?P<ref_id>.*)$', 'places.views.share', name='share'),
    # url(r'^home2/$', 'hello.views.home2', name='home2'),
    
)
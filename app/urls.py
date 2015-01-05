from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^create/','shortener.views.create'), #url where you can see all the urls and create
    url(r'^$','shortener.views.index'), #url where you can see all the urls and create
    url(r'^(?P<shortened_id>\w+)$','shortener.views.follow'),#The redirect of the urls
)

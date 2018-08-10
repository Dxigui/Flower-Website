# -*- coding: utf-8 -*-

from django.conf.urls import url,include

from blog import views as blog_views


urlpatterns = [
    url(r'^$', blog_views.OurStoryView.as_view(), name='ourstory'),
    url(r'^(?P<pk>[0-9]+)/$', blog_views.detail, name='detail'),
    url(r'^search/', include('haystack.urls')),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})$', blog_views.archives, name='archives'),
]
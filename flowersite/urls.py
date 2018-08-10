"""flowersite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include

from flower import views as flower_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', flower_views.index, name='index'),
    url(r'^ourstory/', include('blog.urls')),
    url(r'^flower/', include('flower.urls')),
    # url(r'^search/', include('haystack.urls')),
    url(r'^logo/$', flower_views.logo, name='logo'),
    url(r'^product/$', flower_views.ProductView.as_view(), name='product'),
    url(r'^terminal/$', flower_views.TerminalView.as_view(), name='terminal'),
    url(r'^aboutus/(?P<pk>[0-9]+)/$', flower_views.AboutUs, name='aboutus'),
]

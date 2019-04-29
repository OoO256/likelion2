"""github2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name="home"),
    url(r'^new/$', views.new, name="new"),
    url(r'^post/(?P<index>\d+)/$', views.post_detail, name ='post_detail'),
    url(r'^post/(?P<index>\d+)/edit/$', views.edit, name='edit'),
    url(r'^post/(?P<index>\d+)/remove/$', views.delete, name='delete'),
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




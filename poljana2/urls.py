"""poljana2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from main.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name='main'),
    url(r'^afisha/$', afisha, name='afisha'),
    url(r'^news/$', news, name='news'),
    url(r'^media/$', media, name='media'),
    url(r'^music/$', music, name='music'),
    url(r'^video/$', video, name='video'),
    url(r'^photo/(?P<alboom_id>[-\w]+)/$', photo, name='photo'),
    url(r'^photo/(?P<id>\d+)/$', photo, name='photo'),
    url(r'^photo/$', photo, name='photo'),
    url(r'^contacts/$', contacts, name='contacts'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# -*- coding: utf-8 -*-
"""WASsystem URL Configuration

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
from django.contrib import admin
from WiltseApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.mainpage, name='main'),
    url(r'^notice_write/$',views.notice_write, name='notice_write'),
    url(r'^document/(?P<category_id>\d+)/$',views.doculist, name='document'),
    url(r'^document2/(?P<category_id>\d+)/$',views.docu2list, name='document2'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^noticont/$', views.contview, name='contview'),
    url(r'^docucont/$', views.docuview, name='docuview'),
    url(r'^docu2cont/$', views.docu2view, name='docu2view')
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
from django.conf.urls import include, url
from django.contrib import admin

from .views import index

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^files/', include('files.urls', namespace="files")),
    url(r'^$', index),
]

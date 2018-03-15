from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from rest_framework import routers


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'', include('default.urls')),
    
]

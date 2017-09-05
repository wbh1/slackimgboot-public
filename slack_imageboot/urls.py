from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Example:
    # url(r'^blog/', include('blog.urls')),
    url(r'^img2/', include('img2.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

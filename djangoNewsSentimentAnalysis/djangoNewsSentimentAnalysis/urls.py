from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    #path('',include('basicConcepts.urls')),
    path('', include('NewsApp.urls')),
    path("admin/", admin.site.urls),
]






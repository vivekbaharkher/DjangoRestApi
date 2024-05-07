
from django.contrib import admin
from django.urls import path,include
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('restapp.urls')),
    path('',include('course.urls')),
    path('api-auth',include('restapp.urls')),
    path('recipe/',include('restapp.urls')),
    path('api-token-auth/',views.obtain_auth_token),
    path("__debug__/", include("debug_toolbar.urls")),
]

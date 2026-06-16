from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('projects.urls')),
    path('', include('tasks.urls')),
    path('', include('accounts.urls')),
]
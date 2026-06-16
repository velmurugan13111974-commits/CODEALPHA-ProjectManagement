from django.urls import path
from .views import home, create_project

urlpatterns = [
    path('', home, name='home'),
    path('create-project/', create_project, name='create_project'),
]
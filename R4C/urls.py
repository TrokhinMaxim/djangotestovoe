from django.contrib import admin
from django.urls import path
from robots.views import create_robot

urlpatterns = [
    path('create_robot/', create_robot, name='create_robot'),
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import path
from robots.views import create_robot, summary
from robots import views

urlpatterns = [
    path('create_robot/', create_robot, name='create_robot'),
    path('summary/', views.summary, name='summary'),
    path('download_summary_excel/', views.download_excel_report, name='download_summary_excel'),
    path('admin/', admin.site.urls),
]

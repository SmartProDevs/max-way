from django.urls import path
from .views import main_dashboard
urlpatterns = [
    path('dashboard/',main_dashboard,name="main_dashboard")
]
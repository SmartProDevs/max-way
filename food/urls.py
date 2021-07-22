from django.urls import path
from .views import index, main_order, home_page
urlpatterns = [
    path('',index,name="index"),
    path('home_page/',home_page,name="home_page"),
    path('order/',main_order,name="main_order"),
]
from django.urls import path
from .views import *
urlpatterns = [
    path('',main_dashboard,name="main_dashboard"),
    path('login/', login_page, name="login_page"),
    path('logout/', logout_page, name="logout_page"),

    path('product/list/', product_list, name="product_list"),
    path('product/create/', product_create, name="product_create"),
    path('product/<int:pk>/edit/', product_edit, name='product_edit'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),

    path('category/list/', category_list, name="category_list"),
    path('category/create/', category_create, name="category_create"),
    path('category/<int:pk>/edit/', category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', category_delete, name='category_delete'),
]

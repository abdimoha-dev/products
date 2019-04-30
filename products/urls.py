from django.urls import path
from . import views
app_name = 'products'
urlpatterns=[
    # path('', views.products_view, name='products_view'),
    path('create', views.product_create, name='product_create'),
    path('all_products', views.all_products, name='all_products'),
    path('delete_product/<int:id>/', views.delete_product, name='delete_product'),
    path('productss/<int:id>/', views.product_url, name='product_url'),
    path('products_view', views.products_view, name='products_view'),

]
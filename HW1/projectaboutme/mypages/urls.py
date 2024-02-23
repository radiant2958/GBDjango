from django.urls import path
from . import views

urlpatterns = [
    path('client/<int:client_id>/', views.client_orders, name='client_orders'),
    path('client/<int:client_id>/orders/<int:period>/', views.client_orders_period, name='client_orders_period'),
    path('changed_product/', views.changed_product, name='changed_product'),
    path('product/edit/', views.edit_product, name='edit_product'),
    path('success_url/', views.success_url, name='success_url' ),
    path('product/creat/', views.product_creat_form, name="product_creat_form")
]

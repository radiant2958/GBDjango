from django.urls import path
from . import views

urlpatterns = [
    path('client/<int:client_id>/', views.client_orders, name='client_orders'),
    path('client/<int:client_id>/orders/<int:period>/', views.client_orders_period, name='client_orders_period'),
]

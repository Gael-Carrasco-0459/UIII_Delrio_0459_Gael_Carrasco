# app_Delrio/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_Delrio, name='inicio_delrio'),
    path('ventas/', views.ver_ventas, name='ver_ventas'),
    path('ventas/agregar/', views.agregar_venta, name='agregar_venta'),
    path('ventas/actualizar/<int:pk>/', views.actualizar_venta, name='actualizar_venta'),
    path('ventas/actualizar/realizar/<int:pk>/', views.realizar_actualizacion_venta, name='realizar_actualizacion_venta'),
    path('ventas/borrar/<int:pk>/', views.borrar_venta, name='borrar_venta'),
]
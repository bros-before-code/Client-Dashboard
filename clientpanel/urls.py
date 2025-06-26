from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('client/<int:client_id>/edit/', views.client_edit, name='client_edit'),
    path('clients/add/', views.client_add, name='client_add'),
    path('client/<int:client_id>/delete/', views.client_delete, name='client_delete'),
    path('clients/<int:client_id>/services/', views.manage_services, name='manage_services'),
    path('clients/<int:client_id>/invoice/', views.download_invoice, name='download_invoice'),
]
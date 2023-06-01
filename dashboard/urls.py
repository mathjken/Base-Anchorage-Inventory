from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='dasboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('product/', views.product, name='dashboard-staff'),
    path('order/', views.order, name='dashboard-staff'),
]

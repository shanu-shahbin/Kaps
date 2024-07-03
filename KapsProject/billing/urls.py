from django.urls import path
from . import views

urlpatterns = [
    path('biliing/', views.billing_view, name='billing-home'),
    
]


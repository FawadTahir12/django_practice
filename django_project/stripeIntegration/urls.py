from django.urls import path
from . import views

urlpatterns = [
    path('create-customer/', views.create_customer, name='create-customer'),
    path('create-payment-intent/', views.create_payment_intent, name='create-payment-intent'),
    path('webhook/', views.webhook, name='webhook'),
] 
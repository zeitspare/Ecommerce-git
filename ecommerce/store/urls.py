from django.urls import path
from . import views

urlpatterns = [
    # Baseurl should be left empty
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout")
]
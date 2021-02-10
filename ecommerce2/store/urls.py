from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('<int:id>/<slug:slug>/', views.product_details, name='product_details'),
    path('cart/', views.cart, name="cart"),
    path('checkout', views.checkout, name="checkout"),
    path('<slug:category_slug>/', views.store, name='product-list-by-category'),

]
from django.urls import path
from . import views


app_name = 'store'

urlpatterns = [
    path('', views.store, name='store'),
    path('<int:id>/<slug:slug>/', views.product_details, name='product_details'),
    path('<slug:category_slug>/', views.store, name='products_by_category'),
]
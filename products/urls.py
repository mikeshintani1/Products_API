from django.urls import path
from . import views

urlspatters = [
    path('/', views.products_list),
    path('<int:pk>', views.product_detail),
]
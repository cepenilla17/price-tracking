from django.urls import path
from .views import order, product

urlpatterns = [
    path('order/', order.get_orders),
    path('history/<str:product_id>', order.get_transaction_history),
    path('product/', product.get_products),
]
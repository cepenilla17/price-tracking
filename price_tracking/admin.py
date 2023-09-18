from django.contrib import admin
from .models import (
    Client, Order, Supplier, Product, OrderItem, ProductSupply
)

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['client', 'order_date']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'order', 'quantity', 'unit_price']

@admin.register(ProductSupply)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'supplier', 'inventory', 'unit_price']

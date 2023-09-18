from django.db import models

# Create your models here.

class Client(models.Model):
    class Meta:
        db_table = "client"
        verbose_name_plural = "Clients"

    name = models.CharField(max_length=100, blank=False)
    code = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return str(self.name)

class Supplier(models.Model):
    class Meta:
        db_table = "supplier"
        verbose_name_plural = "Suppliers"

    name = models.CharField(max_length=100, blank=False)
    code = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return "{} ({})".format(str(self.name), self.code)
class Product(models.Model):
    class Meta:
        db_table = "product"
        verbose_name_plural = "Products"

    name = models.CharField(max_length=100, blank=False)
    code = models.CharField(max_length=10, blank=False)
    description = models.TextField(blank=True)
    product_supply = models.ManyToManyField(Supplier, through='ProductSupply')
    # unit_price = models.FloatField()
    # created = models.DateTimeField(auto_now_add=True)
    # updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

class Order(models.Model):
    class Meta:
        db_table = "order"
        verbose_name_plural = "Orders"

    order_date = models.DateTimeField(blank=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}-{}-{}".format(self.id, self.client.code, self.supplier.code)

class OrderItem(models.Model):
    class Meta:
        db_table = "order_item"
        verbose_name_plural = "Order Items"

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=False)
    unit_price = models.FloatField(blank=False)

    def __str__(self):
        return "{}-{}".format(self.order.__str__(), self.product.__str__())

class ProductSupply(models.Model):
    class Meta:
        db_table = "product_supply"
        verbose_name_plural = "Product Supply"
        unique_together = ('product', 'supplier',)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    inventory = models.IntegerField(blank=False)
    unit_price = models.FloatField(blank=False)

    def __str__(self):
        return "{}-{}".format(self.supplier.__str__(), self.product.__str__())

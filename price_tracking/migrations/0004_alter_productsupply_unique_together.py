# Generated by Django 4.2.5 on 2023-09-18 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_tracking', '0003_productsupply_product_product_supply'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='productsupply',
            unique_together={('product', 'supplier')},
        ),
    ]
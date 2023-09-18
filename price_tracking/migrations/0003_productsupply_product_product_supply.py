# Generated by Django 4.2.5 on 2023-09-18 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('price_tracking', '0002_alter_orderitem_options_client_code_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductSupply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.IntegerField()),
                ('unit_price', models.FloatField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price_tracking.product')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='price_tracking.supplier')),
            ],
            options={
                'verbose_name_plural': 'Product supply',
                'db_table': 'product_supply',
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_supply',
            field=models.ManyToManyField(through='price_tracking.ProductSupply', to='price_tracking.supplier'),
        ),
    ]
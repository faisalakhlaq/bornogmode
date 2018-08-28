# Generated by Django 2.1 on 2018-08-28 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_auto_20180828_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChildCarts',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='products.Product')),
                ('age_group', models.CharField(max_length=200)),
                ('length', models.CharField(blank=True, max_length=200, null=True)),
                ('width', models.CharField(blank=True, max_length=200, null=True)),
                ('height', models.CharField(blank=True, max_length=200, null=True)),
                ('weight', models.CharField(blank=True, max_length=200, null=True)),
            ],
            bases=('products.product',),
        ),
    ]
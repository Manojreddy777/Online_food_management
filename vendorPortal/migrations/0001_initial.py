# Generated by Django 4.2.14 on 2024-10-25 17:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vendor_Id', models.CharField(max_length=10, unique=True)),
                ('Vendor_Name', models.CharField(max_length=100)),
                ('Vendor_Phone', models.CharField(max_length=10)),
                ('Total_Customers', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='VendorLogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customers_Delivering', models.ManyToManyField(blank=True, related_name='vendors', to='customers.customer')),
                ('vendor', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vendorPortal.vendor')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-19 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_category_inventory_supplier_demandforecasting_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="products/"),
        ),
    ]

# Generated by Django 3.2.19 on 2023-05-14 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_food_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='sku',
            field=models.CharField(blank=True, max_length=36, null=True, unique=True),
        ),
    ]

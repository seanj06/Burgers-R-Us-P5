# Generated by Django 3.2.19 on 2023-05-14 12:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_food_sku'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='sku',
            field=models.CharField(blank=True, default=uuid.uuid4, max_length=20, null=True),
        ),
    ]

# Generated by Django 3.2.19 on 2023-06-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0009_alter_order_delivery_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.IntegerField(choices=[(0, '13:07'), (15, '13:22'), (30, '13:37'), (45, '13:52'), (60, '14:07'), (75, '14:22')], null=True),
        ),
    ]

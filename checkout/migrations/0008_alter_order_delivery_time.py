# Generated by Django 3.2.19 on 2023-06-09 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_alter_order_delivery_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.IntegerField(choices=[(0, '14:48'), (15, '15:03'), (30, '15:18'), (45, '15:33'), (60, '15:48'), (75, '16:03')], null=True),
        ),
    ]
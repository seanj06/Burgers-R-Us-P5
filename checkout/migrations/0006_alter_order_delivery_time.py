# Generated by Django 3.2.19 on 2023-06-01 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20230531_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.IntegerField(choices=[(0, '12:43'), (15, '12:58'), (30, '13:13'), (45, '13:28'), (60, '13:43'), (75, '13:58')], null=True),
        ),
    ]

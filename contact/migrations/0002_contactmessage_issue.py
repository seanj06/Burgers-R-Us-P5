# Generated by Django 3.2.19 on 2023-06-10 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='issue',
            field=models.CharField(choices=[('General Inquiry', 'General Inquiry'), ('Issue With Food Order', 'Issue With Food Order'), ('Billing Question', 'Billing Question'), ('Food Not Delivered', 'Food Not Delivered'), ('Other', 'Other')], max_length=100, null=True),
        ),
    ]

# Generated by Django 4.1.4 on 2023-01-25 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entries',
            name='Price_Sqft',
        ),
        migrations.RemoveField(
            model_name='entries',
            name='Washroom',
        ),
    ]
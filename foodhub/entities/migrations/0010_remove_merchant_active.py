# Generated by Django 3.1.1 on 2020-12-17 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0009_merchant_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='merchant',
            name='active',
        ),
    ]
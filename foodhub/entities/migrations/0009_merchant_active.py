# Generated by Django 3.1.1 on 2020-12-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entities', '0008_item_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]

# Generated by Django 4.0.1 on 2022-03-01 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0011_itemtype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='customer',
        ),
        migrations.DeleteModel(
            name='itemtype',
        ),
    ]

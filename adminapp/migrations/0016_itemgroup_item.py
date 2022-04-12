# Generated by Django 4.0.1 on 2022-03-01 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0015_delete_item_delete_itemgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemgroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemgroup', models.CharField(max_length=50)),
                ('status', models.CharField(default=None, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=100)),
                ('status', models.CharField(default=None, max_length=30, null=True)),
                ('itemtype_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.itemgroup')),
            ],
        ),
    ]

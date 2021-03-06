# Generated by Django 4.0.1 on 2022-03-06 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0022_delete_loanitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='loanitem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemgroup', models.CharField(max_length=40)),
                ('itemname', models.CharField(max_length=40)),
                ('qty', models.CharField(max_length=40)),
                ('grossweight', models.CharField(max_length=40)),
                ('netweight', models.CharField(max_length=40)),
                ('purity', models.CharField(max_length=40)),
                ('value', models.CharField(max_length=100)),
                ('remarks', models.CharField(max_length=40)),
                ('loanid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.loan')),
            ],
        ),
    ]

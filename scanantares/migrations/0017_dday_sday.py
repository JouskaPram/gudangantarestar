# Generated by Django 3.2.15 on 2023-01-07 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanantares', '0016_double'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Sday',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jumlah', models.CharField(max_length=40)),
            ],
        ),
    ]

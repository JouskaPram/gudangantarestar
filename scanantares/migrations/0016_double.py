# Generated by Django 4.1.5 on 2023-01-06 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanantares', '0015_alter_sortir_scanner_delete_scanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Double',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=40)),
                ('scanner', models.CharField(choices=[('angle', 'angle'), ('latif', 'latif'), ('fazza', 'fazza'), ('antarestar', 'antarestar')], max_length=40, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

# Generated by Django 2.2.12 on 2023-01-02 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=9)),
                ('jumlah', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sortir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(max_length=40)),
                ('jumlah', models.IntegerField(null=True)),
                ('tanggal', models.DateTimeField()),
                ('scanner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scanantares.Scanner')),
            ],
        ),
    ]

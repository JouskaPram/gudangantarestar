# Generated by Django 4.1.5 on 2023-01-06 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scanantares', '0011_remove_sortir_scanner_id_sortir_scanner_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scanner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=9)),
            ],
        ),
        migrations.RemoveField(
            model_name='sortir',
            name='scanner',
        ),
        migrations.AddField(
            model_name='sortir',
            name='scanner_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scanantares.scanner'),
        ),
    ]

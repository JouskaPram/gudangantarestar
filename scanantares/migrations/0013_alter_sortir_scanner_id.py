# Generated by Django 4.1.5 on 2023-01-06 02:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scanantares', '0012_scanner_remove_sortir_scanner_sortir_scanner_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortir',
            name='scanner_id',
            field=models.ForeignKey(max_length=40, null=True, on_delete=django.db.models.deletion.CASCADE, to='scanantares.scanner'),
        ),
    ]
# Generated by Django 2.2.12 on 2023-01-04 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scanantares', '0004_auto_20230104_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sortir',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

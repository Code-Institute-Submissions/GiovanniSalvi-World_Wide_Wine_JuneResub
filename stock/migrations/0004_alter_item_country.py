# Generated by Django 3.2 on 2021-04-25 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20210424_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]

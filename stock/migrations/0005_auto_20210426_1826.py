# Generated by Django 3.2 on 2021-04-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_alter_item_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, default='SOME STRING', upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='image_url',
            field=models.URLField(blank=True, default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='item',
            name='sku',
            field=models.CharField(blank=True, default='SOME STRING', max_length=100),
        ),
        migrations.AlterField(
            model_name='item',
            name='types',
            field=models.CharField(blank=True, default='SOME STRING', max_length=100),
        ),
    ]

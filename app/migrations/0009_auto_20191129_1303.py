# Generated by Django 2.2.7 on 2019-11-29 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_product_information'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='latitud',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='company',
            name='longitud',
            field=models.FloatField(default=0),
        ),
    ]

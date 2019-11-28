# Generated by Django 2.2.7 on 2019-11-27 12:37

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191127_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='PNG', keep_meta=True, null=True, quality=80, size=[600, 600], upload_to='products'),
        ),
    ]
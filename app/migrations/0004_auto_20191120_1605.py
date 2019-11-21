# Generated by Django 2.2.7 on 2019-11-20 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20191120_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_at', 'title'), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together={('category', 'title')},
        ),
    ]

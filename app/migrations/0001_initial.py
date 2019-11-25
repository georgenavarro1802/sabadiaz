# Generated by Django 2.2.7 on 2019-11-25 13:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ('name',),
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('facebook', models.CharField(blank=True, max_length=100, null=True)),
                ('twitter', models.CharField(blank=True, max_length=100, null=True)),
                ('instagram', models.CharField(blank=True, max_length=100, null=True)),
                ('youtube', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Company',
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Gender',
                'verbose_name_plural': 'Genders',
                'db_table': 'genders',
                'ordering': ('name',),
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materials',
                'db_table': 'materials',
                'ordering': ('name',),
                'unique_together': {('name',)},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('information', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(default=0)),
                ('v_price', models.FloatField(default=0)),
                ('p_discount', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('is_new', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('is_bestseller', models.BooleanField(default=False)),
                ('is_onsale', models.BooleanField(default=False)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='products')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Category')),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Gender')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Material')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'db_table': 'products',
                'ordering': ('-created_at', 'title'),
                'unique_together': {('category', 'title')},
            },
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.CharField(max_length=50)),
                ('text2', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='sliders')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Slides',
                'db_table': 'slides',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('testimonial', models.TextField(blank=True, null=True)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='testimonials')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonials',
                'db_table': 'testimonials',
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'WishList',
                'verbose_name_plural': 'WishList',
                'db_table': 'wishList',
                'ordering': ('-created_at',),
                'unique_together': {('user', 'product')},
            },
        ),
    ]

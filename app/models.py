from django.contrib.auth.models import User
from django.db import models

from app.helpers import GENDERS


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = "categories"
        ordering = ('name', )
        unique_together = ('name', )


class Product(models.Model):

    # main fields
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    price = models.FloatField(default=0)
    is_new = models.BooleanField(default=False)
    stock = models.IntegerField(default=0)

    # images fields
    image1 = models.ImageField(upload_to='products', blank=True, null=True)
    image2 = models.ImageField(upload_to='products', blank=True, null=True)
    image3 = models.ImageField(upload_to='products', blank=True, null=True)
    image4 = models.ImageField(upload_to='products', blank=True, null=True)
    image5 = models.ImageField(upload_to='products', blank=True, null=True)
    image6 = models.ImageField(upload_to='products', blank=True, null=True)

    # additional fields
    gender = models.IntegerField(choices=GENDERS, blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    p_discount = models.IntegerField(default=0)
    v_price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.code()} - {self.name}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = "products"
        ordering = ('category', 'name')
        unique_together = ('category', 'name')

    def code(self):
        return str(self.id).zfill(5)


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.code()}"

    class Meta:
        verbose_name = 'WishList'
        verbose_name_plural = 'WishList'
        db_table = "wishList"
        ordering = ('-created_at', )
        unique_together = ('user', 'product')

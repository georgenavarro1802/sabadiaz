from django.contrib.auth.models import User
from django.db import models

from app.helpers import GENDERS, MATERIALS, MATERIAL_GOLD, GENDER_UNISEX
from sabadiaz.settings import STATIC_URL


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

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.name = self.name.capitalize()
        super(Category, self).save(force_insert, force_update, using)


class Product(models.Model):

    # main fields
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    gender = models.IntegerField(choices=GENDERS, default=GENDER_UNISEX, blank=True, null=True)
    material = models.IntegerField(choices=MATERIALS, default=MATERIAL_GOLD, blank=True, null=True)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    information = models.TextField(blank=True, null=True)

    price = models.FloatField(default=0)
    v_price = models.FloatField(default=0)
    p_discount = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)

    # booleans
    is_new = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_bestseller = models.BooleanField(default=False)
    is_onsale = models.BooleanField(default=False)

    # images fields
    image1 = models.ImageField(upload_to='products', blank=True, null=True)
    image2 = models.ImageField(upload_to='products', blank=True, null=True)
    image3 = models.ImageField(upload_to='products', blank=True, null=True)
    image4 = models.ImageField(upload_to='products', blank=True, null=True)
    image5 = models.ImageField(upload_to='products', blank=True, null=True)
    image6 = models.ImageField(upload_to='products', blank=True, null=True)

    created_at = models.DateField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"{self.code()} - {self.title}"

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = "products"
        ordering = ('-created_at', 'title')
        unique_together = ('category', 'title')

    def code(self):
        return str(self.id).zfill(4)

    def get_image1(self):
        return self.image1.url if self.image1 else f"{STATIC_URL}/img/no_images.png"

    def get_image2(self):
        return self.image2.url if self.image2 else f"{STATIC_URL}/img/no_images.png"

    def get_image3(self):
        return self.image3.url if self.image3 else f"{STATIC_URL}/img/no_images.png"

    def get_image4(self):
        return self.image4.url if self.image4 else f"{STATIC_URL}/img/no_images.png"

    def get_image5(self):
        return self.image5.url if self.image5 else f"{STATIC_URL}/img/no_images.png"

    def get_image6(self):
        return self.image6.url if self.image6 else f"{STATIC_URL}/img/no_images.png"

    def get_images_list(self):
        return [
            {
                'image_url': self.get_image1(),
                'is_static': False if self.image1 else True
            },
            {
                'image_url': self.get_image2(),
                'is_static': False if self.image2 else True
            },
            {
                'image_url': self.get_image3(),
                'is_static': False if self.image3 else True
            },
            {
                'image_url': self.get_image4(),
                'is_static': False if self.image4 else True
            },
            {
                'image_url': self.get_image5(),
                'is_static': False if self.image5 else True
            },
            {
                'image_url': self.get_image6(),
                'is_static': False if self.image6 else True
            },
        ]

    def has_images(self):
        return self.image1 or self.image2 or self.image3 or self.image4 or self.image5 or self.image6


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


class HomeSlider(models.Model):
    """
    Examples:
        Ex1
        text1: Flower Diamond
        text2: Collection
        desc: Budget Jewellery Starting At $295.99

        Ex2
        text1: New Diamond
        text2: & Wedding Rings
        desc: Avail 15% off on Making Charges for all Jewellery

        Ex3
        text1: Grace Designer
        text2: Jewellery
        desc: Rings, Occasion Pieces, Pandora & More

    """
    text1 = models.CharField(max_length=50)
    text2 = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sliders')

    def __str__(self):
        return self.text1

    class Meta:
        verbose_name = 'HomePage Slider'
        verbose_name_plural = 'HomePage Sliders'
        db_table = "home_sliders"

    def get_image(self):
        return self.image.url if self.image else f"{STATIC_URL}/img/slide.jpg"

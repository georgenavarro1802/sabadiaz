from PIL import Image

from django.contrib.auth.models import User
from django.db import models
from django_resized import ResizedImageField

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

    def get_my_first_products(self):
        return self.product_set.all()[:10]

    def get_available_products(self):
        return self.product_set.filter(stock__gt=0)

    def count_of_available_products(self):
        return self.get_available_products().count()

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.name = self.name.capitalize()
        super(Category, self).save(force_insert, force_update, using)


class Material(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materials'
        db_table = "materials"
        ordering = ('name', )
        unique_together = ('name', )

    def get_available_products(self):
        return self.product_set.filter(stock__gt=0)

    def count_of_available_products(self):
        return self.get_available_products().count()

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.name = self.name.capitalize()
        super(Material, self).save(force_insert, force_update, using)


class Gender(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'
        db_table = "genders"
        ordering = ('name', )
        unique_together = ('name', )

    def get_available_products(self):
        return self.product_set.filter(stock__gt=0)

    def count_of_available_products(self):
        return self.get_available_products().count()

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        self.name = self.name.capitalize()
        super(Gender, self).save(force_insert, force_update, using)


class Product(models.Model):

    # main fields
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)

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

    # images fields
    image1 = ResizedImageField(size=[370, 370], upload_to='products', blank=True, null=True)
    image1_b = ResizedImageField(size=[570, 570], upload_to='products', blank=True, null=True)
    image2 = ResizedImageField(size=[370, 370], upload_to='products', blank=True, null=True)
    image2_b = ResizedImageField(size=[570, 570], upload_to='products', blank=True, null=True)
    image3 = ResizedImageField(size=[370, 370], upload_to='products', blank=True, null=True)
    image3_b = ResizedImageField(size=[570, 570], upload_to='products', blank=True, null=True)
    image4 = ResizedImageField(size=[370, 370], upload_to='products', blank=True, null=True)
    image4_b = ResizedImageField(size=[570, 570], upload_to='products', blank=True, null=True)
    image5 = ResizedImageField(size=[370, 370], upload_to='products', blank=True, null=True)
    image5_b = ResizedImageField(size=[570, 570], upload_to='products', blank=True, null=True)
    image6 = ResizedImageField(size=[370, 370], upload_to='products', blank=True, null=True)
    image6_b = ResizedImageField(size=[570, 570], upload_to='products', blank=True, null=True)

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

    def get_image1_b(self):
        return self.image1_b.url if self.image1_b else f"{STATIC_URL}/img/no_images.png"

    def get_image2(self):
        return self.image2.url if self.image2 else f"{STATIC_URL}/img/no_images.png"

    def get_image2_b(self):
        return self.image2_b.url if self.image2_b else f"{STATIC_URL}/img/no_images.png"

    def get_image3(self):
        return self.image3.url if self.image3 else f"{STATIC_URL}/img/no_images.png"

    def get_image3_b(self):
        return self.image3_b.url if self.image3_b else f"{STATIC_URL}/img/no_images.png"

    def get_image4(self):
        return self.image4.url if self.image4 else f"{STATIC_URL}/img/no_images.png"

    def get_image4_b(self):
        return self.image4_b.url if self.image4_b else f"{STATIC_URL}/img/no_images.png"

    def get_image5(self):
        return self.image5.url if self.image5 else f"{STATIC_URL}/img/no_images.png"

    def get_image5_b(self):
        return self.image5_b.url if self.image5_b else f"{STATIC_URL}/img/no_images.png"

    def get_image6(self):
        return self.image6.url if self.image6 else f"{STATIC_URL}/img/no_images.png"

    def get_image6_b(self):
        return self.image6_b.url if self.image6_b else f"{STATIC_URL}/img/no_images.png"

    def get_images_list(self):
        return [
            {
                'image_url': self.get_image1(),
                'imageb_url': self.get_image1_b(),
                'is_static': False if self.image1 else True,
                'is_static_b': False if self.image1_b else True,
            },
            {
                'image_url': self.get_image2(),
                'imageb_url': self.get_image2_b(),
                'is_static': False if self.image2 else True,
                'is_static_b': False if self.image2_b else True,
            },
            {
                'image_url': self.get_image3(),
                'imageb_url': self.get_image3_b(),
                'is_static': False if self.image3 else True,
                'is_static_b': False if self.image3_b else True,
            },
            {
                'image_url': self.get_image4(),
                'imageb_url': self.get_image4_b(),
                'is_static': False if self.image4 else True,
                'is_static_b': False if self.image4_b else True,
            },
            {
                'image_url': self.get_image5(),
                'imageb_url': self.get_image5_b(),
                'is_static': False if self.image5 else True,
                'is_static_b': False if self.image5_b else True,
            },
            {
                'image_url': self.get_image6(),
                'imageb_url': self.get_image6_b(),
                'is_static': False if self.image6 else True,
                'is_static_b': False if self.image6_b else True,
            },
        ]

    def has_images(self):
        return self.image1 or self.image2 or self.image3 or self.image4 or self.image5 or self.image6

    def get_reviews(self):
        return self.review_set.all()

    def count_of_reviews(self):
        return self.get_reviews().count()


class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.code()}"

    class Meta:
        verbose_name = 'WishList'
        verbose_name_plural = 'WishList'
        db_table = "wishlist"
        ordering = ('-created_at', )
        unique_together = ('user', 'product')


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.SmallIntegerField(default=5)
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.code()}"

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
        db_table = "reviews"
        ordering = ('-created_at', )


# WebSite Pages and Content
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    address = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    twitter = models.CharField(max_length=100, blank=True, null=True)
    instagram = models.CharField(max_length=100, blank=True, null=True)
    youtube = models.CharField(max_length=100, blank=True, null=True)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Company'
        db_table = "company"

    def get_logo(self):
        return self.logo.url if self.logo else f"{STATIC_URL}/img/logo/logo.png"

    @staticmethod
    def get_available_products():
        return Product.objects.filter(stock__gt=0)

    def count_of_available_products(self):
        return self.get_available_products().count()

    def get_available_new_products(self):
        return self.get_available_products().filter(is_new=True)

    def count_of_available_new_products(self):
        return self.get_available_new_products().count()

    def get_available_featured_products(self):
        return self.get_available_products().filter(is_featured=True)

    def count_of_available_featured_products(self):
        return self.get_available_featured_products().count()

    def get_available_bestseller_products(self):
        return self.get_available_products().filter(is_bestseller=True)

    def count_of_available_bestseller_products(self):
        return self.get_available_bestseller_products().count()


class Slide(models.Model):
    text1 = models.CharField(max_length=50)
    text2 = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    image = models.ImageField(upload_to='sliders')

    def __str__(self):
        return self.text1

    class Meta:
        verbose_name = 'Slide'
        verbose_name_plural = 'Slides'
        db_table = "slides"

    def get_image(self):
        return self.image.url if self.image else f"{STATIC_URL}/img/slide.jpg"

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        super().save()
        if self.image:
            img = Image.open(self.image.path)
            if img.width > 1920 or img.height > 670:
                img.thumbnail((1920, 670))
                img.save(self.image.path)

        super(Slide, self).save(force_insert, force_update, using)


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    testimonial = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='testimonials', blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'
        db_table = "testimonials"

    def get_avatar(self):
        return self.avatar.url if self.avatar else f"{STATIC_URL}/img/default-avatar.png"

    def save(self, force_insert=False, force_update=False, using=None, **kwargs):
        super().save()
        if self.avatar:
            img = Image.open(self.avatar.path)
            if img.width > 100 or img.height > 100:
                img.thumbnail((100, 100))
                img.save(self.avatar.path)

        super(Testimonial, self).save(force_insert, force_update, using)

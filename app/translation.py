from modeltranslation.translator import register, TranslationOptions

from app.models import Category, Material, Gender, Product, Company, Slide, Testimonial


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('name',)


@register(Material)
class MaterialTranslation(TranslationOptions):
    fields = ('name',)


@register(Gender)
class GenderTranslation(TranslationOptions):
    fields = ('name',)


@register(Product)
class ProductTranslation(TranslationOptions):
    fields = ('title', 'description')


@register(Slide)
class SlideTranslation(TranslationOptions):
    fields = ('text1', 'text2', 'description')


@register(Testimonial)
class TestimonialTranslation(TranslationOptions):
    fields = ('testimonial',)


@register(Company)
class CompanyTranslation(TranslationOptions):
    fields = ('description',)

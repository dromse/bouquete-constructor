from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.urls import reverse


User = get_user_model()


def get_product_url(obj, viewname):
    ct_model = obj.__class__._meta.model_name
    return reverse(viewname, kwargs={'ct_model': ct_model, 'slug': obj.slug})


class LatestProductsManager:
    
    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        products = []
        with_respect_to = kwargs.get('with_respect_to')
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class()._base_manager.all().order_by('-id')[:5]
            products.extend(model_products)

        if with_respect_to:
            ct_model = ContentType.objects.filter(model=with_respect_to) 
            if ct_model.exists():
                if with_respect_to in args:
                    return sorted(
                        products, key=lambda x: x.__class__._meta.model_name.startswith(with_respect_to), reverse=True
                    )

        return products
        

class LatestProducts:
     
    objects = LatestProductsManager()


class Product(models.Model):

    class Meta:
        abstract = True
    
    name = models.CharField(verbose_name='Name', max_length=50)
    slug = models.SlugField(unique=True)
    amount = models.IntegerField(verbose_name='Amount')
    price = models.DecimalField(verbose_name='Price', max_digits=9, decimal_places=2)
    image = models.ImageField(verbose_name='Image')

    def __str__(self):
        return self.name


class Flower(Product):
    def __str__(self):
        return f'{self.name}'

    def get_absolute_url(self):
        return get_product_url(self, 'product_detail')


class CartProduct(models.Model):

    user = models.ForeignKey('Customer', verbose_name='Customer', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Cart', on_delete=models.CASCADE, related_name='related_products')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    qty = models.PositiveIntegerField(default=1)
    final_price = models.DecimalField(verbose_name='Final Price', decimal_places=2, max_digits=9)


    def __str__(self):
        return f'Flowers: {self.content_object.name} (for the cart)'


class Cart(models.Model):

    owner = models.ForeignKey('Customer', verbose_name='Owner', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, related_name='related_chart')
    total_products = models.PositiveIntegerField(default=0)
    final_price = models.DecimalField(verbose_name='Final Price', decimal_places=2, max_digits=9)
    in_order = models.BooleanField(default=False)
    for_anonymous_user = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.id}'


class Customer(models.Model):

    user = models.ForeignKey(User, verbose_name='User', on_delete=models.CASCADE)
    phone = models.CharField(max_length=28, verbose_name='Phone')
    address = models.CharField(max_length=255, verbose_name='Address')


    def __str__(self):
        return f'Customer: {self.user.first_name}'


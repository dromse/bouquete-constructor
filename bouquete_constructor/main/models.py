from django.db import models


class Category(models.Model):

    name = models.CharField(verbose_name='Name of category')

    def __str__(self) -> str:
        return self.name


class Product(models.Model):

    name = models.CharField(verbose_name='Name', max_length=50)
    amount = models.IntegerField(verbose_name='Amount')
    price = models.DecimalField(verbose_name='Price', max_digits=9, decimal_places=2)
    image = models.ImageField(verbose_name='Image')

    def __str__(self) -> str:
        return self.name


from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin
from .models import *


class FlowerAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Flower, FlowerAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
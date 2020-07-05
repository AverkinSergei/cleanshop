from django.db import models
from django.utils.translation import ugettext as _


class NamedModel(models.Model):
    name = models.CharField(_('name'), max_length=200)

    class Meta:
        abstract = True


class Category(NamedModel):
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class ProductManager(models.Manager):

    def published(self):
        return self.filter(published=True)


class Product(NamedModel):
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=12)
    description = models.TextField(_('description'), null=True, blank=True)
    published = models.BooleanField(_('published'), default=False)

    objects = ProductManager()

    class Meta:
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def to_dict(self):
        return {
            'name': self.name, 'price': self.price, 'description': self.description, 'published': self.published,
        }

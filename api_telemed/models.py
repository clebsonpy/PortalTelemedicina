from django.db import models
from django.utils import timezone as tz
from accounts.models import User


class Product(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=255, null=True, default=None)
    description = models.TextField(verbose_name='Descrição', null=True)
    price = models.DecimalField(verbose_name='Preço', max_digits=6, decimal_places=2)
    created_date = models.DateField(verbose_name='Data de criação', default=tz.now)


class CartItem(models.Model):
    product = models.ForeignKey(verbose_name='Produto', to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Quantidade', default=1)
    price = models.DecimalField(verbose_name='Preço', max_digits=8, decimal_places=2)


class Order(models.Model):
    user = models.ForeignKey(verbose_name='Usuário', to=User,
                             related_name='order_user', on_delete=models.CASCADE
                             )
    cart_item = models.ForeignKey(verbose_name='Carrinho', to=CartItem,
                                  related_name='order_item', on_delete=models.CASCADE
                                  )
    created_date = models.DateField(verbose_name='Data de criação', default=tz.now)

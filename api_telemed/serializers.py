from rest_framework import serializers
from .models import Product, CartItem, Order
from drf_writable_nested import WritableNestedModelSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):

    product = ProductSerializer(many=False)

    class Meta:
        model = CartItem
        fields = '__all__'


class OrderSerializer(WritableNestedModelSerializer):

    cart_item = CartItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['user', 'cart_item']

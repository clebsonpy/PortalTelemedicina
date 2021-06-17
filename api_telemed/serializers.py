from rest_framework import serializers
from .models import Product, CartItem, Order
from drf_writable_nested import WritableNestedModelSerializer


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):

    # product = ProductSerializer(many=False)

    class Meta:
        model = CartItem
        exclude = ['order']
        extra_fields = {'id': {'read_only': True}}


class OrderSerializer(WritableNestedModelSerializer):

    cart_item = CartItemSerializer(many=True, source='cart_order')

    class Meta:
        model = Order
        fields = ['user', 'created_date', 'cart_item']
        extra_fields = {'created_date': {'read_only': True}}

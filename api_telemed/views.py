from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer


# Create your views here.
class ProductViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    @action(methods=['get'], detail=False)
    def search(self, request, pk=None):
        return None

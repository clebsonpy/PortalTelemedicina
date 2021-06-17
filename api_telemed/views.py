from django.shortcuts import render
from rest_framework import mixins, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user_id_data = request.data['user']
        print(request.data)
        if request.user.id != user_id_data:
            return Response(data={'message': 'user id passed in body different from logged user id!'})
        
        return super(OrderViewSet, self).create(request=request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def search(self, request, pk=None):
        return None

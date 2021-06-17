from django.shortcuts import render
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime


from .models import Product, Order
from .serializers import ProductSerializer, OrderSerializer


# Create your views here.
class ProductViewSet(mixins.CreateModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, )


class OrderViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        user_id_data = request.data['user']
        if request.user.id != user_id_data:
            return Response(data={'message': 'user id passed in body different from logged user id!'})
        
        return super(OrderViewSet, self).create(request=request, *args, **kwargs)

    @action(methods=['get'], detail=False)
    def search(self, request, pk=None):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if start_date:
            start_date = datetime.strptime(start_date, '%d/%m/%Y')
            self.queryset = self.queryset.filter(created_date__gte=start_date)

        if end_date:
            end_date = datetime.strptime(end_date, '%d/%m/%Y')
            self.queryset = self.queryset.filter(created_date__lte=end_date)

        return super(OrderViewSet, self).list(request=request)

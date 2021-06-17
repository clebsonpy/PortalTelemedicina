from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductViewSet, OrderViewSet

router = SimpleRouter()
router.register('products', ProductViewSet, basename='products')
router.register('orders', viewset=OrderViewSet, basename='order')

urlpatterns = [
    path('', include(router.urls))
]

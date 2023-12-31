from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend 
from rest_framework.filters import SearchFilter
from logistic.models import Product, Stock
from logistic.serializers import ProductSerializer, StockSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # при необходимости добавьте параметры фильтрации
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['title', 'description']
    
class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    
    def get_queryset(self):
        if product := self.request.query_params.get('products'):
            return Stock.objects.filter(products__id=product)
        else:
            return self.queryset
        
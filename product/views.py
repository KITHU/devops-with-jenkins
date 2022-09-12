from product.models import Product
from rest_framework import viewsets
from product.serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

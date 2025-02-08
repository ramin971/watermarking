from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .tasks import add_watermark





class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        product = serializer.save()
        add_watermark.delay(product.image.path, product.id)

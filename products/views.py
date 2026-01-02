from rest_framework import viewsets, filters

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsOwnerOrAdmin

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    permission_classes = [IsOwnerOrAdmin]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'description']

    ordering_fields = ['price', 'created_at']
    ordering = ['created_at']
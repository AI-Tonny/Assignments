from rest_framework import viewsets, filters

from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']

    ordering_fields = ['created_at']
    ordering = ['created_at']

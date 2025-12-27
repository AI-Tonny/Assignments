from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone

from datetime import timedelta

from .models import News
from .serializers import NewsSerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticatedOrReadOnly])
    def in_last_24_hours(self, request):
        time_threshold = timezone.now() - timedelta(hours=24)

        news_in_last_24_hours = News.objects.filter(created_at__gte=time_threshold)
        serializer = self.get_serializer(news_in_last_24_hours, many=True)

        return Response(serializer.data)

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['content']

    ordering_fields = ['title', 'created_at']
    ordering = ['created_at']

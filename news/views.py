from rest_framework import viewsets, filters

from .models import News
from .serializers import NewsSerializer
from .permissions import IsJournalistCanOnlyCreate

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    permission_classes = [IsJournalistCanOnlyCreate]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['title', 'content']

    ordering_fields = ['created_at']
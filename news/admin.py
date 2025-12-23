from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image_url', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
    ordering = ('-created_at',)
    readonly_fields = ('created_at', )

from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=800)
    image_url = models.URLField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
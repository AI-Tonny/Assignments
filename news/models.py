from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    title = models.CharField(max_length=125)
    content = models.TextField(max_length=1500)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class News(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=250)
    content = models.TextField(max_length=2500)
    image_url = models.URLField(max_length=800)
    created_at = models.DateTimeField(auto_now_add=True)
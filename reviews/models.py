from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    id = models.AutoField(primary_key=True)

    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"
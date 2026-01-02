from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=75)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500, null=True)
    is_available = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    photo_url = models.URLField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(max_length=75)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=500, null=True)
    photo_url = models.URLField(max_length=250, blank=True, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ['-created_at', '-price', '-rating']
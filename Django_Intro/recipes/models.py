from django.db import models

from .enums import RecipeType

class Recipe(models.Model):
    id = models.AutoField(primary_key=True)

    title = models.CharField(
        max_length=75,
        null=False
    )
    author = models.CharField(
        max_length=65,
        null=True
    )
    type = models.CharField(
        max_length=25,
        choices=[(tag.name, tag.value) for tag in RecipeType],
        default=RecipeType.FIRST_COURSES.name
    )
    description = models.TextField(
        max_length=1500,
        null=False
    )
    video_uri = models.CharField(
        max_length=250,
        null=True
    )
    ingredients = models.TextField(
        max_length=350,
        null=False
    )
    cuisine = models.CharField(
        max_length=45,
        null=True
    )
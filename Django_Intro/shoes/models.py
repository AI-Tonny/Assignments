from django.db import models

from .enums import ShoeGender, ShoeType, ShoeColor, ShoeSize

class Shoe(models.Model):
    id = models.AutoField(primary_key=True)

    gender = models.CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in ShoeGender],
        default=ShoeGender.MALE.name
    )
    type = models.CharField(
        max_length=20,
        choices=[(tag.name, tag.value) for tag in ShoeType],
        default=ShoeType.SNEAKERS.name
    )
    color = models.CharField(
        max_length=30,
        choices=[(tag.name, tag.value) for tag in ShoeColor],
        default=ShoeColor.WHITE.name
    )
    size = models.CharField(
        max_length=30,
        choices=[(tag.name, tag.value) for tag in ShoeSize],
        default=ShoeSize.MEDIUM.name
    )
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=False
    )
    manufacture = models.CharField(
        max_length=75,
        null=True
    )
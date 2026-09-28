from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)

    code = models.CharField(
        max_length=30,
        unique=True,
    )

    quantity = models.IntegerField()

    def __str__(self):
        return self.name

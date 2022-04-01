from django.db import models


# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    product_image = models.CharField(max_length=255, default = "no image")
    product_review = models.CharField(max_length=255)
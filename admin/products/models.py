from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(blank=True, null=True, max_length=120)
    price = models.DecimalField(decimal_places=2, max_digits=1000)
    feature = models.BooleanField(default=True)

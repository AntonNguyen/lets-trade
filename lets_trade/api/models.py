from django.db import models

# Create your models here.
from django.db import models

class Item(models.Model):
    item_name = models.CharField(max_length=80)
    city = models.CharField(max_length=30)
    postal_code = models.CharField(max_length=30)
    description = models.TextField()
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
	user = models.ForeignKey(User)
	name = models.CharField(max_length=80, blank=False)
	description = models.TextField()
	address = models.CharField(max_length=80)
	address2 = models.CharField(max_length=30)
	city = models.CharField(max_length=60)
	code = models.CharField(max_length=10)

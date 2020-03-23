from django.db import models

# Create your models here.
class db(models.Model):
	roll_no = models.CharField(max_length=10)
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	department = models.CharField(max_length=100)
	year = models.IntegerField()
	course = models.CharField(max_length=100)
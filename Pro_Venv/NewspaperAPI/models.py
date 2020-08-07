from django.db import models
from django.urls import reverse
from django.db.models import Model
from django.contrib.auth.models import User
import datetime

Language =(
    ("Spanish", "Spanish"),
    ("English", "English"),
)

Publication =(
    ("Weekdays", "Weekdays"),
    ("Saturday", "Saturday"),
    ("Sunday", "Sunday"),
)

Payment =(
    ("Paid", "Paid"),
    ("Not_Paid", "Not_Paid"),
)

class Newspaper (models.Model):
		newspaper = models.CharField(max_length=50)
		language = models.CharField(max_length=50, choices=Language)
		wh_price = models.DecimalField(max_digits=6,decimal_places=2)
		sa_price = models.DecimalField(max_digits=6,decimal_places=2)
		description = models.CharField(max_length=50)
		company = models.CharField(max_length=50)
		publication = models.CharField(max_length=50, choices=Publication)
		def __str__(self):
			return self.newspaper

class Consumer (models.Model):
		name = models.CharField(max_length=32)
		address = models.CharField(max_length=32)
		telephone = models.CharField(max_length=32)
		email = models.CharField(max_length=32)
		ac_no = models.IntegerField(default=0)
		def __str__(self):
			return self.name

class Intake(models.Model):
		added_date 	= models.DateField(max_length=32,auto_now_add=True)
		newspaper 	= models.ForeignKey(Newspaper, on_delete=models.CASCADE)
		qty		  	= models.IntegerField(default=0)
		qty_return 	= models.IntegerField(default=0)
		total 		= models.IntegerField(default=0)
	def save(self, *args, **kwargs):
		    super(Intake, self).save(*args, **kwargs)
		    self.total = self.newspaper.wh_price * self.qty
		    self.save()

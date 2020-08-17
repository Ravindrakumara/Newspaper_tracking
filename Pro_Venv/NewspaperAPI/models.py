from django.db import models
from django.urls import reverse
from django.db.models import Model
from django.contrib.auth.models import User
from datetime import datetime
from celery.schedules import crontab
from celery.task import periodic_task
import os
from apscheduler.schedulers.background import BackgroundScheduler


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
		#ac_no = models.CharField(blank=True,max_length=254) #IntegerField(default=0)
		def __str__(self):
			return self.name

class Intake(models.Model):
		added_date 	= models.DateField(max_length=32,auto_now_add=True)
		newspaper 	= models.ForeignKey(Newspaper,on_delete=models.CASCADE)
		qty		  	= models.IntegerField(default=0)
		qty_return 	= models.IntegerField(default=0)
		total 		= models.IntegerField(default=0)
		def save(self,*args,**kwargs):
			self.total = self.newspaper.wh_price * (self.qty - self.qty_return)
			super(Intake,self).save(*args, **kwargs)



class Consumer_order(models.Model):
		name	= models.ForeignKey(Consumer, on_delete=models.CASCADE)
		ac_no	= models.CharField(max_length=32)
		newspaper = models.ManyToManyField(Newspaper,related_name="Consumer_ac_no")
		added_date = models.DateField(max_length=32,auto_now_add=True)

		def __str__(self):
			return str(self.ac_no)


class Daily_Cart(models.Model):
        ac_no       = models.CharField(max_length=32)
        newspaper   = models.CharField(max_length=32)
        added_date  = models.DateTimeField(max_length=32,auto_now_add=True)

        def __str__(self):
        		return str(self.added_date)

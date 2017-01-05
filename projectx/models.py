# models.py
# Defines the structure of the database.

# https://docs.djangoproject.com/en/1.10/topics/db/models/

from django.db import models
from django.contrib.auth.models import User

class Club(models.Model):
	name = models.CharField(max_length=64, default="")
	email = models.EmailField(max_length=128, blank=True, null=True)
	website = models.URLField(max_length=256, blank=True, null=True)
	meeting_times = models.CharField(max_length=256, blank=True, null=True)

	# officers that can manage the club
	president = models.IntegerField(null=True, blank=True)
	treasurer = models.IntegerField(null=True, blank=True)
	icc_rep = models.IntegerField(null=True, blank=True)
	
	def __str__(self):
		return self.name

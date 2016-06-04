from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField(max_length=200)
	portada = models.ImageField(blank=True)
	content = models.TextField()
	date = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.title

class Email(models.Model):
	name = models.CharField(max_length=60)
	email = models.EmailField()

	def __unicode__(self):
		return self.name
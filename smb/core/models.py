from django.db import models

# Create your models here.


class Municipality(models.Model):

	
	name = models.CharField(max_length=200)
	description = models.TextField()
	#states = models.CharField(max_length=1, choices=STATES)
	lat = models.CharField(max_length=10)
	log = models.CharField(max_length=10)
	avatar = models.FileField(upload_to='/avatar')


def __str__(self):
	  return self.name





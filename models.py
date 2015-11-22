from django.db import models

# Create your models here.
class Poll(models.Model): 
	question = models.CharField(max_length=1000)

	def __str__(self):
		return self.question
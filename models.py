from django.db import models

# Create your models here.
class Poll(models.Model): 
	question = models.CharField(max_length=1000)
	isMultiSelect = models.BooleanField(default=False)

	def __str__(self):
		return self.question

class Choice(models.Model):
	text = models.CharField(max_length=500)
	isSelected = models.BooleanField(default=False)
	votes = models.IntegerField(default=0)
	poll = models.ForeignKey(Poll, related_name='choices')

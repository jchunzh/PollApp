from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Poll, Choice

class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ['id', 'text', 'isSelected', 'votes']
		depth = 2

class PollSerializer(serializers.ModelSerializer):
	choices = ChoiceSerializer(many=True)
	class Meta:
		model = Poll
		fields = ['id', 'question', 'isMultiSelect', 'choices']

	def create(self, data):
		choices_data = data.pop('choices')
		poll = Poll.objects.create(**data)
		
		for choice in choices_data:
			Choice.objects.create(poll=poll, **choice)
			
		return poll
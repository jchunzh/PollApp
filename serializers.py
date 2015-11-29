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


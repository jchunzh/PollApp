from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Poll, Choice
from PollApp.Repositories.PollRepository import PollRepository

class ChoiceSerializer(serializers.ModelSerializer):
	uniqueId = serializers.CharField(required=False, allow_blank=True)

	class Meta:
		model = Choice
		fields = ['text', 'isSelected', 'votes', 'uniqueId']
		depth = 2

class PollSerializer(serializers.ModelSerializer):
	choices = ChoiceSerializer(many=True)
	uniqueId = serializers.CharField(required=False, allow_blank=True)

	class Meta:
		model = Poll
		fields = ['question', 'isMultiSelect', 'choices', 'uniqueId']

	def create(self, data):
		pollRepo = PollRepository()
		return pollRepo.createPoll(data)

	def validate(self, data):
		if (not data["choices"] or len(data["choices"]) < 2):
			raise serializers.ValidationError("At least two choices are required")

		return data
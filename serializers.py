from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Poll, Choice
import uuid
import base64
from PollApp.repositories.PollRepository import PollRepository

class ChoiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Choice
		fields = ['id','text', 'isSelected', 'votes']
		depth = 2

class PollSerializer(serializers.ModelSerializer):
	choices = ChoiceSerializer(many=True)
	class Meta:
		model = Poll
		fields = ['question', 'isMultiSelect', 'choices', 'uniqueId']

	def create(self, data):
		pollRepo = PollRepository()
		return pollRepo.createPoll(data)
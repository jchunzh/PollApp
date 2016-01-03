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
		fields = ['question', 'isMultiSelect', 'choices', 'uuid64']

	def getUnusedUuid(self):
		while True:
			candidateUuid = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8')[0:22]
			existingPoll = Poll.objects.filter(uuid64=candidateUuid)
				
			if not existingPoll:
				break
		
		return candidateUuid
	

	def create(self, data):
		pollRepo = PollRepository()
		return pollRepo.createPoll(data)
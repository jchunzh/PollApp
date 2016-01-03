from PollApp.models import Poll, Choice
import uuid
import base64

class PollRepository():
	def _getUnusedUuid(self):
		while True:
			candidateUuid = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8')[0:22]
			existingPoll = Poll.objects.filter(uuid64=candidateUuid)
				
			if not existingPoll:
				break
		
		return candidateUuid
	

	def createPoll(self, pollDic):
		choices_data = pollDic.pop('choices')
		
		poll = Poll(**pollDic)
		poll.uuid64 = self._getUnusedUuid()
		poll.save()
		
		for choice in choices_data:
			Choice.objects.create(poll=poll, **choice)
		return poll
		
	def getPollByUniqueId(self, uniqueId):
		poll = Poll.objects.get(uuid64=uniqueId)
		return poll
from PollApp.models import Choice
from PollApp.utility.UniqueIdGenerator import UniqueIdGenerator

class ChoiceRepository():
	def __init__(self):
		self._uniqueIdGenerator = UniqueIdGenerator()
	
	def voteForChoices(self, choiceUniqueIds):
		choices = Choice.objects.filter(uniqueId__in=choiceUniqueIds)
		
		for c in choices:
			print(c)
			c.votes += 1
			c.save()
		
	def create(self, poll, **choice):
		choice = Choice(**choice)
		choice.uniqueId = self._getUnusedChoiceUuid()
		choice.poll = poll
		choice.save()
		
		return choice
		
		
	def _getUnusedChoiceUuid(self):
		while True:
			candidateUuid = self._uniqueIdGenerator.createUniqueId()
			existingPoll = Choice.objects.filter(uniqueId=candidateUuid)
				
			if not existingPoll:
				break
		
		return candidateUuid
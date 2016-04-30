from PollApp.models import Choice
from PollApp.Utility.UniqueIdGenerator import UniqueIdGenerator

class ChoiceRepository():
	def __init__(self):
		self._uniqueIdGenerator = UniqueIdGenerator()
	
	def voteForChoices(self, choiceUniqueIds):
		choices = Choice.objects.filter(uniqueId__in=choiceUniqueIds)
		
		for c in choices:
			c.votes += 1
			c.save()
		
	def create(self, choice):
		choice.save()

	def getChoiceByUniqueId(self, uniqueId):
		try:
			choice = Choice.objects.get(uniqueId=uniqueId)
		except Choice.DoesNotExist:
			return None

		return choice
from PollApp.models import Poll, Choice
from PollApp.Utility.UniqueIdGenerator import UniqueIdGenerator

class PollRepository():
	
	def __init__(self):
		self._uniqueIdGenerator = UniqueIdGenerator()

	def create(self, poll):
		poll.save()
		
	def getPollByUniqueId(self, uniqueId):
		try:
			poll = Poll.objects.get(uniqueId=uniqueId)
		except Poll.DoesNotExist:
			return None

		return poll
from PollApp.Facades.ChoiceFacade import ChoiceFacade
from PollApp.Repositories.PollRepository import PollRepository
from PollApp.Utility.UniqueIdGenerator import UniqueIdGenerator

class PollFacade():
	def __init__(self):
		self._uniqueIdGenerator = UniqueIdGenerator()
		self._choiceFacade = ChoiceFacade()
		self._pollRepository = PollRepository()

	def create(self, poll, choices):
		poll.uniqueId = self._getUnusedPollUniqueId()
		self._pollRepository.create(poll)
		
		for choice in choices:
			self._choiceFacade.create(choice, poll)

	def _getUnusedPollUniqueId(self):
		for i in range(100):
			candidatePollUniqueId = self._uniqueIdGenerator.createUrlSafeUniqueId()
			existingPoll = self._pollRepository.getPollByUniqueId(candidatePollUniqueId)

			if existingPoll is None:
				break
		
		return candidatePollUniqueId

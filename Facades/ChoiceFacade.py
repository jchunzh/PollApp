from PollApp.Utility.UniqueIdGenerator import UniqueIdGenerator
from PollApp.Repositories.ChoiceRepository import ChoiceRepository

class ChoiceFacade():
	_uniqueIdGenerator = None
	_choiceRepository = None

	def __init__(self):
		self._uniqueIdGenerator = UniqueIdGenerator()
		self._choiceRepository = ChoiceRepository()

	def create(self, choice, poll):
		choice.uniqueId = self._getUnusedChoiceUuid()
		choice.poll = poll
		self._choiceRepository.create(choice)

	def _getUnusedChoiceUuid(self):
		while True:
			candidateUuid = self._uniqueIdGenerator.createUniqueId()
			existingChoice = self._choiceRepository.getChoiceByUniqueId(candidateUuid)

			if existingChoice is None:
				break
		
		return candidateUuid
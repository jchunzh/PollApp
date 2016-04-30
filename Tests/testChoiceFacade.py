from unittest.mock import MagicMock, create_autospec
from django.test import TestCase
from PollApp.Tests.Utility import Utility
from PollApp.models import Choice, Poll
from PollApp.Facades.ChoiceFacade import ChoiceFacade
from PollApp.Repositories.ChoiceRepository import ChoiceRepository
from PollApp.Utility.UniqueIdGenerator import UniqueIdGenerator

class ChoiceFacadeTestCase(TestCase, Utility):
	def setUp(self):
		self.sut = ChoiceFacade()
		self.sut._choiceRepository = create_autospec(ChoiceRepository, spec_set=True, instance=True)
		self.sut._choiceRepository.getChoiceByUniqueId.side_effect = [None]
		self.sut._uniqueIdGenerator = create_autospec(UniqueIdGenerator, spec_set=True, instance=True)

	def test_when_creating_a_choice_then_poll_is_associated_with_the_choice(self):
		expectedChoice = Choice()
		expectedPoll = Poll()

		self.sut.create(expectedChoice, expectedPoll)

		self.assertEqual(expectedChoice.poll, expectedPoll)
		self.sut._choiceRepository.create.assert_called_once_with(expectedChoice)

	def test_when_creating_a_choice_then_a_unique_id_is_created(self):
		repeatId = self.getUniqueId()
		expectedUniqueId = self.getUniqueId()
		expectedChoice = Choice()

		self.sut._uniqueIdGenerator.createUniqueId.side_effect = [repeatId, expectedUniqueId]
		self.sut._choiceRepository.getChoiceByUniqueId.side_effect = [Choice(), None]
		self.sut.create(expectedChoice, Poll())
		
		self.assertEqual(expectedChoice.uniqueId, expectedUniqueId)
		self.sut._choiceRepository.create.assert_called_once_with(expectedChoice)
from unittest.mock import create_autospec, call
from django.test import TestCase
from PollApp.Tests.Utility import Utility
from PollApp.Facades.PollFacade import PollFacade
from PollApp.Facades.ChoiceFacade import ChoiceFacade
from PollApp.Repositories.PollRepository import PollRepository
from PollApp.Utility.UniqueIdGenerator import UniqueIdGenerator
from PollApp.models import Poll, Choice

class testCreate(TestCase, Utility):
	def setUp(self):
		self.sut = PollFacade()
		self.sut._pollRepository = create_autospec(PollRepository, spec_set=True, instance=True)
		self.sut._pollRepository.getPollByUniqueId.side_effect = [None]
		self.sut._choiceFacade = create_autospec(ChoiceFacade, spec_set=True, instance=True)
		self.sut._uniqueIdGenerator = create_autospec(UniqueIdGenerator, spec_set=True, instance=True)

	def test_when_creating_a_poll_then_a_unique_id_is_created(self):
		expectedPoll = Poll()
		repeatPollId = 0
		expectedPollUniqueId = 1

		self.sut._uniqueIdGenerator.createUrlSafeUniqueId.side_effect = [repeatPollId, expectedPollUniqueId]
		self.sut._pollRepository.getPollByUniqueId.side_effect = [Poll(), None]

		self.sut.create(expectedPoll, [Choice()])

		self.assertEqual(expectedPoll.uniqueId, expectedPollUniqueId)

	def test_choices_are_saved(self):
		expectedPoll = Poll()
		expectedChoice1 = Choice()
		expectedChoice2 = Choice()
		expectedChoice3 = Choice()

		self.sut.create(expectedPoll, [expectedChoice1, expectedChoice2, expectedChoice3])

		calls = [
			call(expectedChoice1, expectedPoll), 
			call(expectedChoice2, expectedPoll), 
			call(expectedChoice3, expectedPoll)
		]

		self.sut._choiceFacade.create.assert_has_calls(calls, any_order=False)

	def test_poll_is_saved(self):
		expectedPoll = Poll()

		self.sut.create(expectedPoll, [Choice()])

		self.sut._pollRepository.create.assert_called_once_with(expectedPoll)
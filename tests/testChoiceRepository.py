from django.test import TestCase
from PollApp.models import Poll, Choice
from PollApp.repositories.ChoiceRepository import ChoiceRepository
from unittest.mock import MagicMock
from PollApp.tests.Utility import Utility

class ChoiceRepositoryTestCase(TestCase, Utility):
	sut = None;
	poll = None;
	
	def setUp(self):
		self.sut = ChoiceRepository()
		self.poll = Poll(uniqueId = self.getUniqueId())
		self.poll.save()
		
	def test_when_voting_for_a_choice_then_the_votes_count_is_incremented(self):
		choice = self._createTestChoice(self.getUniqueId(), 1, self.poll)
		
		self.sut.voteForChoices([choice.uniqueId])
		
		self.assertEqual(Choice.objects.get(pk=choice.id).votes, 2)
		
	def test_when_voting_for_multiple_choices_then_votes_for_every_choice_is_incremented(self):
		choices = [
		self._createTestChoice(self.getUniqueId(), 3, self.poll),
		self._createTestChoice(self.getUniqueId(), 4, self.poll)
		]
		
		self.sut.voteForChoices([choices[0].uniqueId, choices[1].uniqueId])
		
		self.assertEqual(Choice.objects.get(pk=choices[0].id).votes, 4)
		self.assertEqual(Choice.objects.get(pk=choices[1].id).votes, 5)

	def test_when_creating_a_choice_then_a_unique_id_is_created(self):
		repeatId = self.getUniqueId()
		self.sut._uniqueIdGenerator.createUniqueId = MagicMock(return_value = repeatId)
		self.sut.create(self.poll, **{
		})
		
		self.sut._uniqueIdGenerator.createUniqueId = MagicMock(side_effect = [repeatId, self.getUniqueId()])
		result = self.sut.create(self.poll, **{
			'text': 'test',
			'isSelected': True
		})
		
		self.assertNotEqual(result.uniqueId, repeatId)
		self.assertTrue(result.isSelected)
		self.assertEqual('test', result.text)

		
	def _createTestChoice(self, uniqueId, votes, poll):
		choice = Choice(uniqueId = uniqueId, votes = votes, poll = poll)
		choice.save()
		
		return choice;
from django.test import TestCase
from PollApp.models import Poll, Choice
from PollApp.serializers import PollSerializer
from PollApp.repositories.PollRepository import PollRepository
from unittest.mock import MagicMock

class PollRepositoryTestCase(TestCase):
	sut = None
	data = None
	
	def setUp(self):
		self.sut = PollRepository()
		self.pollDict = {
			'question' : 'question text',
			'isMultiSelect' : False
		}
		
		self.choices = [
			{
				'text': 'choice1',
				'isSelected' : False,
				
			},
			{
				'text': 'choice2',
				'isSelected' : False
			}
		]
	
	def test_when_creating_new_poll_then_new_poll_guid_is_created(self):
		result = self.sut.createPoll(self.pollDict, self.choices)
		self.assertTrue(isinstance(result.uniqueId, str))
		self.assertIsNotNone(result.uniqueId)
		self.assertEqual(result.id, Poll.objects.get(uniqueId=result.uniqueId).id)
		
	def test_when_creating_new_poll_and_new_polls_uniqueId_already_exists_then_a_new_uniqueId_is_created(self):
		self.sut._uniqueIdGenerator.createUrlSafeUniqueId = MagicMock(return_value = 1)
		self.sut.createPoll(self.pollDict, self.choices)
		
		self.sut._uniqueIdGenerator.createUrlSafeUniqueId = MagicMock(side_effect = [1, 2])
		result = self.sut.createPoll(self.pollDict, self.choices)
		
		self.assertEqual(2, self.sut._uniqueIdGenerator.createUrlSafeUniqueId.call_count)
		
	def test_when_retrieving_poll_by_unique_id_then_the_correct_poll_is_returned(self):
		uniqueId = "1234'"
		poll = Poll()
		poll.uniqueId = uniqueId
		poll.save();
		
		result = self.sut.getPollByUniqueId(uniqueId)
	
		self.assertEqual(poll.id, result.id)
	

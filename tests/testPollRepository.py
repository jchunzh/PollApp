from django.test import TestCase
from PollApp.models import Poll, Choice
from PollApp.serializers import PollSerializer
from PollApp.repositories.PollRepository import PollRepository
from unittest.mock import MagicMock
from PollApp.tests.Utility import Utility

class PollRepositoryTestCase(TestCase, Utility):
	sut = None
	data = None
	
	def setUp(self):
		self.sut = PollRepository()
		self.pollDict = {
			'question' : 'question text',
			'isMultiSelect' : False
		}
	
	def test_when_creating_new_poll_then_new_poll_guid_is_created(self):
		result = self.sut.createPoll(self.pollDict)
		self.assertTrue(isinstance(result.uniqueId, str))
		self.assertIsNotNone(result.uniqueId)
		self.assertEqual(result.id, Poll.objects.get(uniqueId=result.uniqueId).id)
		
	def test_when_creating_new_poll_and_new_polls_uniqueId_already_exists_then_a_new_uniqueId_is_created(self):
		repeatId = self.getUniqueId()
		self.sut._uniqueIdGenerator.createUrlSafeUniqueId = MagicMock(return_value = repeatId)
		self.sut.createPoll(self.pollDict)
		
		self.sut._uniqueIdGenerator.createUrlSafeUniqueId = MagicMock(side_effect = [repeatId, self.getUniqueId()])
		result = self.sut.createPoll(self.pollDict)
		
		self.assertEqual(2, self.sut._uniqueIdGenerator.createUrlSafeUniqueId.call_count)
		
	def test_when_retrieving_poll_by_unique_id_then_the_correct_poll_is_returned(self):
		uniqueId = self.getUniqueId()
		poll = Poll()
		poll.uniqueId = uniqueId
		poll.save();
		
		result = self.sut.getPollByUniqueId(uniqueId)
	
		self.assertEqual(poll.id, result.id)
		
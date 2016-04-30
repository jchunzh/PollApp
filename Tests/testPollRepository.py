from django.test import TestCase
from PollApp.models import Poll, Choice
from PollApp.serializers import PollSerializer
from PollApp.Repositories.PollRepository import PollRepository
from unittest.mock import MagicMock
from PollApp.Tests.Utility import Utility

class PollRepositoryTestCase(TestCase, Utility):
	sut = None
	data = None
	
	def setUp(self):
		self.sut = PollRepository()
		
	def test_when_retrieving_poll_by_unique_id_then_the_correct_poll_is_returned(self):
		uniqueId = self.getUniqueId()
		poll = Poll()
		poll.uniqueId = uniqueId
		poll.save();
		
		result = self.sut.getPollByUniqueId(uniqueId)
	
		self.assertEqual(poll.id, result.id)

	def test_when_retrieveing_poll_by_unique_id_then_none_is_returned_when_there_is_no_match(self):
		poll = self.sut.getPollByUniqueId(-1)

		self.assertEqual(poll, None)
		
from django.test import TestCase
from PollApp.models import Poll, Choice
from PollApp.serializers import PollSerializer
from PollApp.repositories.PollRepository import PollRepository

class PollRepositoryTestCase(TestCase):
	sut = None
	data = None
	
	def setUp(self):
		self.sut = PollRepository()
		self.data = self._createData()
		
		
	def _createData(self):
		choices = [
			{
				'text': 'choice1',
				'isSelected' : False,
				
			},
			{
				'text': 'choice2',
				'isSelected' : False
			}
		]
		data = {
			'question' : 'question text',
			'choices' : choices,
			'isMultiSelect' : False
		}
		
		return data
	
	def test_when_creating_new_poll_then_new_poll_guid_is_created(self):
		result = self.sut.createPoll(self.data)
		self.assertTrue(isinstance(result.uuid64, str))
		self.assertIsNotNone(result.uuid64)
		self.assertEqual(result.id, Poll.objects.get(uuid64=result.uuid64).id)
		
	def test_when_retrieving_poll_by_unique_id_then_the_correct_poll_is_returned(self):
		uniqueId = "1234'"
		poll = Poll()
		poll.uuid64 = uniqueId
		poll.save();
		
		result = self.sut.getPollByUniqueId(uniqueId)
	
		self.assertEqual(poll.id, result.id)
	

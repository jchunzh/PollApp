from django.test import TestCase
from PollApp.models import Poll, Choice
from PollApp.Repositories.PollRepository import PollRepository
from PollApp.Repositories.ChoiceRepository import ChoiceRepository
from PollApp.Validators.PollValidator import PollValidator

class ValidateNewPollTestCase(TestCase):
	sut = None
	
	def setUp(self):
		self.sut = PollValidator()

	def test_when_question_text_length_is_greater_than_max_then_error_is_returned(self):
		questionText = 'a' * 1001
		poll = Poll(question=questionText)
		
		results = self.sut.validateNewPoll(poll).getErrors()
		
		self.assertEqual(len(results), 1)
		self.assertEqual(results[0], self.sut.QUESTION_TOO_LONG)
		
	def test_when_question_text_length_is_0_then_error_is_returned(self):
		poll = Poll(question='')
		results = self.sut.validateNewPoll(poll).getErrors()
		
		self.assertEqual(len(results), 1)
		self.assertEqual(results[0], self.sut.QUESTION_REQUIRED)
		
	def test_when_question_text_is_none_then_error_is_returned(self):
		poll = Poll(question=None)
		results = self.sut.validateNewPoll(poll).getErrors()
		
		self.assertEqual(len(results), 1)
		self.assertEqual(results[0], self.sut.QUESTION_REQUIRED)

		
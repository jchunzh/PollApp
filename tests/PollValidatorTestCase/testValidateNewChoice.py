from django.test import TestCase
from PollApp.models import Poll, Choice
from PollApp.repositories.PollRepository import PollRepository
from PollApp.repositories.ChoiceRepository import ChoiceRepository
from PollApp.Validators.ChoiceValidator import ChoiceValidator

class testValidateNewChoice(TestCase):
	def setUp(self):
		self.sut = ChoiceValidator()
	
	def test_when_a_single_choices_text_is_greater_than_max_then_error_is_returned(self):
		tooLongText = 'a' * 501
		choice = Choice(text=tooLongText)
		
		results = self.sut.validateNewChoices([choice]).choicesValidationResults
		
		self.assertEqual(len(results), 1)
		self.assertIn(self.sut.CHOICE_TOO_LONG, results[0].getErrors())
		self.assertEqual(len(results[0].getErrors()), 1)
	
	def test_when_many_choices_text_are_greater_than_max_then_error_is_returned_in_the_choices_order(self):
		tooLongText = 'a' * 501
		choices = [
			Choice(text=tooLongText),
			Choice(text=tooLongText),
			Choice(text=tooLongText),
			Choice(text=tooLongText)
		]
		
		results = self.sut.validateNewChoices(choices).choicesValidationResults
		
		self.assertEqual(len(results), 4)
		self.assertIn(self.sut.CHOICE_TOO_LONG, results[0].getErrors())
		self.assertEqual(len(results[0].getErrors()), 1)

		self.assertIn(self.sut.CHOICE_TOO_LONG, results[1].getErrors())
		self.assertEqual(len(results[1].getErrors()), 1)

		self.assertIn(self.sut.CHOICE_TOO_LONG, results[2].getErrors())
		self.assertEqual(len(results[2].getErrors()), 1)

		self.assertIn(self.sut.CHOICE_TOO_LONG, results[3].getErrors())
		self.assertEqual(len(results[3].getErrors()), 1)
		
	def test_when_some_choices_text_are_greater_than_max_then_error_is_returned_in_the_choices_order(self):
		tooLongText = 'a' * 501
		validLengthText = 'a' * 20
		choices = [
			Choice(text=tooLongText),
			Choice(text=validLengthText),
			Choice(text=tooLongText),
			Choice(text=tooLongText)
		]
		
		results = self.sut.validateNewChoices(choices).choicesValidationResults
		
		self.assertEqual(len(results), 4)
		self.assertIn(self.sut.CHOICE_TOO_LONG, results[0].getErrors())
		self.assertEqual(len(results[0].getErrors()), 1)

		self.assertIn('', results[1].getErrors())
		self.assertEqual(len(results[1].getErrors()), 1)

		self.assertIn(self.sut.CHOICE_TOO_LONG, results[2].getErrors())
		self.assertEqual(len(results[2].getErrors()), 1)

		self.assertIn(self.sut.CHOICE_TOO_LONG, results[3].getErrors())
		self.assertEqual(len(results[3].getErrors()), 1)

	def test_single_choice_is_length_0_then_error(self):
		choice = Choice(text='')
		
		result = self.sut.validateNewChoices([choice]).getCollectiveValidationResult().getErrors()
		
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0], self.sut.CHOICE_REQUIRED)
		
		
	def test_single_choice_is_none_then_error(self):
		choice = Choice(text=None)
		
		result = self.sut.validateNewChoices([choice]).getCollectiveValidationResult().getErrors()
		
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0], self.sut.CHOICE_REQUIRED)
		
	def test_all_choices_are_length_0_then_error(self):
		choices = [
			Choice(text=''),
			Choice(text=''),
			Choice(text='')
		]
		
		result = self.sut.validateNewChoices(choices).getCollectiveValidationResult().getErrors()
		
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0], self.sut.CHOICE_REQUIRED)
		
	def test_all_choices_are_none_then_error(self):
		choices = [
			Choice(text=None),
			Choice(text=None),
			Choice(text=None)
		]
		
		result = self.sut.validateNewChoices(choices).getCollectiveValidationResult().getErrors()
		
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0], self.sut.CHOICE_REQUIRED)
		
	def test_at_least_one_choice_is_valid_length_then_no_error(self):
		choices = [
			Choice(text=None),
			Choice(text=''),
			Choice(text='valid text')
		]
		
		result = self.sut.validateNewChoices(choices).getCollectiveValidationResult().getErrors()
		
		self.assertEqual(len(result), 0)

	def test_when_number_of_choices_are_over_max_then_error_is_returned(self):
		choices = []
		
		for i in range(31):
			choices.append(Choice(text='valid text'))
			
		result = self.sut.validateNewChoices(choices).getCollectiveValidationResult().getErrors()
		
		self.assertEqual(len(result), 1)
		self.assertEqual(result[0], self.sut.TOO_MANY_CHOICES)
		
	def test_when_number_of_choices_are_over_max_but_none_empty_choices_are_not_then_no_errors(self):
		choices = []
		
		for i in range(40):
			if (i % 2) == 0:
				choices.append(Choice(text='valid text'))
			else:
				choices.append(Choice(text=''))
			
		result = self.sut.validateNewChoices(choices).getCollectiveValidationResult().getErrors()
		
		self.assertEqual(len(result), 0)
from django.test import TestCase
from PollApp.serializers import PollSerializer
import copy

class testPollSerializer(TestCase):
	def setUp(self):
		self.validData = {
			"question" : "test",
			"uniqueId" : "",
			"choices" : [
			{
				"text" : "choice 1"
			},
			{
				"text" : "choice 2"
			}]
		}

	def test_question_required(self):
		invalidData = copy.deepcopy(self.validData)
		invalidData["question"] = ""

		sut = PollSerializer(data=invalidData)

		self.assertFalse(sut.is_valid())
		self.assertIn("This field may not be blank.", sut.errors["question"])

	def test_question_max_length_enforced(self):
		invalidData = copy.deepcopy(self.validData)
		invalidData["question"] = "a" * 1001

		sut = PollSerializer(data=invalidData)

		self.assertFalse(sut.is_valid())
		self.assertIn("Ensure this field has no more than 1000 characters.", sut.errors["question"])

	def test_only_one_non_empty_choice_is_invalid(self):
		invalidData = copy.deepcopy(self.validData)
		invalidData["choices"] = [
			{
				"text" : "choice 1"
			},
			{
				"text" : ""
			}
		]

		sut = PollSerializer(data=invalidData)

		self.assertFalse(sut.is_valid())
		choiceErrors = [error for dictionary in sut.errors["choices"] for errorList in dictionary.values() for error in errorList]
		self.assertIn("This field may not be blank.", choiceErrors)

	def test_only_one_choice_is_invalid(self):
		invalidData = copy.deepcopy(self.validData)
		invalidData["choices"] = [
			{
				"text" : "choice 1"
			},
		]

		sut = PollSerializer(data=invalidData)

		self.assertFalse(sut.is_valid())
		self.assertIn("At least two choices are required", sut.errors["non_field_errors"])

	def test_no_choice_is_invalid(self):
		invalidData = copy.deepcopy(self.validData)
		invalidData["choices"] = [
		]

		sut = PollSerializer(data=invalidData)

		self.assertFalse(sut.is_valid())
		self.assertIn("At least two choices are required", sut.errors["non_field_errors"])

	def test_unique_id_not_required(self):
		sut = PollSerializer(data=self.validData)
		self.assertTrue(sut.is_valid())

	
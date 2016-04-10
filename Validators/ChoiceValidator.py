from PollApp.models import Poll, Choice
from PollApp.Models.ValidationResult import ValidationResult
from PollApp.Models.ChoiceCollectionValidationResults import ChoiceCollectionValidationResults

class ChoiceValidator():
	CHOICE_TOO_LONG = 'Too long'
	CHOICE_REQUIRED = 'Required'
	TOO_MANY_CHOICES = 'Too many'
	CHOICE_LENGTH = 500
	MAX_CHOICES_NUM = 30
	
	def validateNewChoices(self, choices):
		collectionValidationResults = ChoiceCollectionValidationResults()
		numberOfEmptyChoices = 0
		
		for choice in choices:
			if self._isTextEmpty(choice.text):
				numberOfEmptyChoices += 1
			
			collectionValidationResults.addChoicesValidationResult(self._getChoiceValidation(choice))
			
		collectionValidationResults.setCollectiveValidationResult(self._validateCollective(choices, numberOfEmptyChoices))
		
		return collectionValidationResults
	
	def _isTextEmpty(self, text):
		return (text is None) or (len(text) == 0)
	
	def _getChoiceValidation(self, choice):
		validationResult = ValidationResult()
		
		if choice.text is not None and len(choice.text) > self.CHOICE_LENGTH:
			validationResult.addError(self.CHOICE_TOO_LONG)
		else:
			validationResult.addError('')

		return validationResult
		
		
	def _validateCollective(self, choices, numberOfEmptyChoices):
		validationResult = ValidationResult()
		
		if numberOfEmptyChoices == len(choices):	
			validationResult.addError(self.CHOICE_REQUIRED)
			
		if (len(choices) - numberOfEmptyChoices) > self.MAX_CHOICES_NUM:
			validationResult.addError(self.TOO_MANY_CHOICES)
			
		return validationResult

from PollApp.models import Poll, Choice
from PollApp.Models.ValidationResult import ValidationResult

class PollValidator():
	QUESTION_TOO_LONG = 'Question must be under 1000 characters'
	QUESTION_REQUIRED = 'Question is required'
	QUESTION_MAX_SIZE = 1000
	
	def validateNewPoll(self, poll):
		validationResult = ValidationResult()
		
		if (poll.question is not None and len(poll.question) > self.QUESTION_MAX_SIZE):
			validationResult.addError(self.QUESTION_TOO_LONG)	
			
		if (poll.question is None or len(poll.question) == 0):
			validationResult.addError(self.QUESTION_REQUIRED)
					
		return validationResult
	
	def _validateQuestionLength(self, questionText):
		pass
		
	def _validateChoiceTextLength(self, choiceText):
		pass
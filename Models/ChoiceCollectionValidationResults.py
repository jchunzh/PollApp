from PollApp.Models.ValidationResult import ValidationResult

class ChoiceCollectionValidationResults():
	def __init__(self):
		self.collectiveValidationResult = ValidationResult()
		self.choicesValidationResults = []
		
	
	def getCollectiveValidationResult(self):
		return self.collectiveValidationResult
	
	def setCollectiveValidationResult(self, validationResult):
		self.collectiveValidationResult = validationResult;
	
	def addChoicesValidationResult(self, choiceValidationResult):
		self.choicesValidationResults.append(choiceValidationResult)
	
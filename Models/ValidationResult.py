class ValidationResult():
	def __init__(self):
		self.errors = []

	def addError(self, error):
		self.errors.append(error)
		
	def getErrors(self):
		return self.errors
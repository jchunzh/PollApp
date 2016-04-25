import uuid;

class Utility():
	_uniqueId = 'a';
	
	def getUniqueId(self):
		Utility._uniqueId += 'a'
		return Utility._uniqueId
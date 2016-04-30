import uuid
import base64

class UniqueIdGenerator():
	def _createdStripped64(self):
		stripped64 = base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8')[0:22]
		return stripped64.replace('-', '').replace('_', '')


	def createUrlSafeUniqueId(self):
		candidate = self._createdStripped64()
			
		return candidate[0:10]
		
	def createUniqueId(self):
		return base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8')[0:22]
		
			
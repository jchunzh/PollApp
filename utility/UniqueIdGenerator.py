import uuid
import base64

class UniqueIdGenerator():
	def createUrlSafeUniqueId(self):
		return base64.urlsafe_b64encode(uuid.uuid4().bytes).decode('utf-8')[0:22]
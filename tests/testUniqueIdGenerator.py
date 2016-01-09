from django.test import TestCase
from PollApp.utility.UniqueIdGenerator import UniqueIdGenerator

class UniqueIdGeneratorTestCase(TestCase):
	sut = None;
	
	def setUp(self):
		self.sut = UniqueIdGenerator()
		
	def test_when_generating_unique_id_then_length_is_6(self):
		uniqueId = self.sut.createUrlSafeUniqueId()
		
		self.assertEqual(6, len(uniqueId))
		
	def test_when_generating_unique_id_then_does_not_contain_illegal_characters(self):
		illegalChar = ['+', '-', '_', '\\', '/', '=']
		uniqueId = self.sut.createUrlSafeUniqueId()
		
		for c in illegalChar:
			self.assertNotIn(c, uniqueId)
import unittest
import question2 as q2


class TestQuestion2(unittest.TestCase):
	def test_validate_files(self):
		#length(input files)<2
		with self.assertRaises(SystemExit): 
			q2.validate_files(['f2.txt'])

		#length(input files)<2
		with self.assertRaises(SystemExit): 
			q2.validate_files([])
		
		#length(input files)>2
		with self.assertRaises(SystemExit):    
			q2.validate_files(['n1.txt','n2.txt','f1.txt','f3.txt'])

		#2 invalid files
		with self.assertRaises(SystemExit):    
			q2.validate_files(['n1.txt','n2.txt'])

		#1 invalid file
		with self.assertRaises(SystemExit):    
			q2.validate_files(['n1.txt','f3.txt'])

		#2 valid files
		self.assertEqual(q2.validate_files(['f1.txt','f3.txt']),['f1.txt','f3.txt'])


	def test_compare_files(self):
		self.assertEqual(q2.compare_files('f1.txt','f3.txt'),9988)

	
if __name__ == '__main__':
	unittest.main(TestQuestion2())

import unittest
import question1 as q1

class TestQuestion1(unittest.TestCase):

	def test_distinct_integers(self):
		self.assertEqual(q1.distinct_integers([1, 2, 0]), 3)
		self.assertEqual(q1.distinct_integers([4, 1, 3, 4, 2]), 3)
		self.assertEqual(q1.distinct_integers([5,6,4,7,1,8,7,5,3]), 4)


	def test_distinct_integers_modified(self):
		self.assertEqual(q1.distinct_integers_modified([1, 2, 0]), 3)
		self.assertEqual(q1.distinct_integers_modified([4, 1, 3, 4, 2]), 3)
		self.assertEqual(q1.distinct_integers_modified([5,6,4,7,1,8,7,5,3]), 4)
		

if __name__ == '__main__':
	unittest.main(TestQuestion1())


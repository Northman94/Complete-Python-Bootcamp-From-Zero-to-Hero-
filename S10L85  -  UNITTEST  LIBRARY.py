
import unittest
import S10L85_2

class TestCap(unittest.TestCase):

	def test_one_word(self):
		text = 'python'
		result = S10L85_2.cap_text(text)
		self.assertEqual(result, "Python")


	def test_multiple_words(self):
		text = 'monty python'
		result = S10L85_2.cap_text(text)
		self.assertEqual(result, "Monty Python")


	def test_all_words(self):
		text = 'monty python'
		result = S10L85_2.cap_all_text(text)
		self.assertEqual(result, "Monty Python")




if __name__ == '__main__':
	unittest.main()
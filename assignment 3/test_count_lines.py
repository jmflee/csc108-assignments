import unittest
from poetry_functions import count_lines

class Test_count_lines(unittest.TestCase):
	
	def test_one_string_one_end_character(self):
		'''Test count_lines with single line and one ending characters'''
		actual = count_lines(['Hello World\n'])
		expected = 1
		self.assertEqual(actual,expected)
	
	def test_one_string_two_end_character(self):
		'''Test count_lines with single line of test and no ending characters'''
		actual = count_lines(['Hello World\n\n'])
		expected = 1
		self.assertEqual(actual,expected)
		
	def test_one_string_many_end_character(self):
		'''Test count_lines with single line of test and no ending characters'''
		actual = count_lines(['Hello World\n\n\n\n\n\n\n\n\n\n'])
		expected = 1
		self.assertEqual(actual,expected)
	
	def test_two_strings_two_end_character(self):
		'''Test count_lines with single line of test and no ending characters'''
		actual = count_lines(['Hello World\n', 'I am alive!\n'])
		expected = 2
		self.assertEqual(actual,expected)
	
	def test_multiple_strings_multiple_end_character(self):
		'''Test count_lines with single line of test and no ending characters'''
		actual = count_lines(['Hello World\n','\n     ', 'I am alive!\n', '\n'])
		expected = 2
		self.assertEqual(actual,expected)
	
	def test_five_strings_five_end_character(self):
		'''Test count_lines with single line of test and no ending characters'''
		actual = count_lines(['Hello World\n', 'I am alive!\n',\
		'This is a dream\n', 'A pancake, a pancake!\n', \
		'My kingdome for a pancake!\n'])
		expected = 5
		self.assertEqual(actual,expected)
	
	def test_fake_string(self):
		'''Test count_lines with single line of test and no ending characters'''
		actual = count_lines(['Hello World\n', 'I am alive!\n',\
		'This is a dream\n','     \n     ', 'A pancake, a pancake!\n', \
		'My kingdome for a pancake!\n'])
		expected = 5
		self.assertEqual(actual,expected)
	
	def test_empty_string(self):
		'''Test count_lines with single line of test and no ending characters'''
		actual = count_lines(['Hello World\n', 'I am alive!\n',\
		'This is a dream\n', '      ', 'A pancake, a pancake!\n', \
		'My kingdome for a pancake!\n'])
		expected = 5
		self.assertEqual(actual,expected)
		
	def test_empty_string(self):
		'''Test count_lines with single line of test and no ending characters'''
		actual = count_lines(['Hello World\n', 'I am alive!\n',\
		'This is a dream\n', '      ', 'A pancake, a pancake!\n', \
		'My kingdome for a pancake!\n'])
		expected = 5
		self.assertEqual(actual,expected)

if __name__ == '__main__':
	unittest.main(exit=False)
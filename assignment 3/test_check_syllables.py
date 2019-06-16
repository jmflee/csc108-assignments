import unittest
from poetry_functions import check_syllables

class Test_check_syllables(unittest.TestCase):
	
	def test_less_syllables(self):
		'''Test check_syllables with poem_lines pattern and word_to_phonemes'''
		
		poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
		pattern = ([5, 5, 4], ['*', '*', '*'])
		word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],\
		'GAP': ['G', 'AE1', 'P'],\
		'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],\
		'LEADS': ['L', 'IY1', 'D', 'Z'],\
		'WITH': ['W', 'IH1', 'DH'],\
		'LINE': ['L', 'AY1', 'N'],\
		'THEN': ['DH', 'EH1', 'N'],\
		'THE': ['DH', 'AH0'], \
		'A': ['AH0'], \
		'FIRST': ['F', 'ER1', 'S', 'T'], \
		'ENDS': ['EH1', 'N', 'D', 'Z'],\
		'POEM': ['P', 'OW1', 'AH0', 'M'],\
		'OFF': ['AO1', 'F']}
		actual = check_syllables(poem_lines,pattern,word_to_phonemes)
		expected = ['With a gap before the next.', 'Then the poem ends.']
		self.assertEqual(actual, expected)
		
	def test_right_syllables(self):
		'''Test check_syllables with poem_lines pattern and word_to_phonemes'''
		
		poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
		pattern = ([5, 7, 5], ['*', '*', '*'])
		word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],\
		'GAP': ['G', 'AE1', 'P'],\
		'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],\
		'LEADS': ['L', 'IY1', 'D', 'Z'],\
		'WITH': ['W', 'IH1', 'DH'],\
		'LINE': ['L', 'AY1', 'N'],\
		'THEN': ['DH', 'EH1', 'N'],\
		'THE': ['DH', 'AH0'], \
		'A': ['AH0'], \
		'FIRST': ['F', 'ER1', 'S', 'T'], \
		'ENDS': ['EH1', 'N', 'D', 'Z'],\
		'POEM': ['P', 'OW1', 'AH0', 'M'],\
		'OFF': ['AO1', 'F']}
		actual = check_syllables(poem_lines,pattern,word_to_phonemes)
		expected = []
		self.assertEqual(actual, expected)
	
	def test_float_number(self):
		'''Test check_syllables with poem_lines pattern and word_to_phonemes'''
		
		poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
		pattern = ([5, 7.0, 5.0], ['*', '*', '*'])
		word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],\
		'GAP': ['G', 'AE1', 'P'],\
		'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],\
		'LEADS': ['L', 'IY1', 'D', 'Z'],\
		'WITH': ['W', 'IH1', 'DH'],\
		'LINE': ['L', 'AY1', 'N'],\
		'THEN': ['DH', 'EH1', 'N'],\
		'THE': ['DH', 'AH0'], \
		'A': ['AH0'], \
		'FIRST': ['F', 'ER1', 'S', 'T'], \
		'ENDS': ['EH1', 'N', 'D', 'Z'],\
		'POEM': ['P', 'OW1', 'AH0', 'M'],\
		'OFF': ['AO1', 'F']}
		actual = check_syllables(poem_lines,pattern,word_to_phonemes)
		expected = []
		self.assertEqual(actual, expected)
		
	def test_more_syllables(self):
		'''Test check_syllables with poem_lines pattern and word_to_phonemes'''
		
		poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
		pattern = ([5, 7, 6], ['*', '*', '*'])
		word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],\
		'GAP': ['G', 'AE1', 'P'],\
		'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],\
		'LEADS': ['L', 'IY1', 'D', 'Z'],\
		'WITH': ['W', 'IH1', 'DH'],\
		'LINE': ['L', 'AY1', 'N'],\
		'THEN': ['DH', 'EH1', 'N'],\
		'THE': ['DH', 'AH0'], \
		'A': ['AH0'], \
		'FIRST': ['F', 'ER1', 'S', 'T'], \
		'ENDS': ['EH1', 'N', 'D', 'Z'],\
		'POEM': ['P', 'OW1', 'AH0', 'M'],\
		'OFF': ['AO1', 'F']}
		actual = check_syllables(poem_lines,pattern,word_to_phonemes)
		expected = ['Then the poem ends.']
		self.assertEqual(actual, expected)
		
	def test_negative_nmber(self):
		'''Test check_syllables with poem_lines pattern and word_to_phonemes'''
		
		poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
		pattern = ([5, 7, -5], ['*', '*', '*'])
		word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],\
		'GAP': ['G', 'AE1', 'P'],\
		'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],\
		'LEADS': ['L', 'IY1', 'D', 'Z'],\
		'WITH': ['W', 'IH1', 'DH'],\
		'LINE': ['L', 'AY1', 'N'],\
		'THEN': ['DH', 'EH1', 'N'],\
		'THE': ['DH', 'AH0'], \
		'A': ['AH0'], \
		'FIRST': ['F', 'ER1', 'S', 'T'], \
		'ENDS': ['EH1', 'N', 'D', 'Z'],\
		'POEM': ['P', 'OW1', 'AH0', 'M'],\
		'OFF': ['AO1', 'F']}
		actual = check_syllables(poem_lines,pattern,word_to_phonemes)
		expected = ['Then the poem ends.']
		self.assertEqual(actual, expected)
		
	def test_string_instead_of_number(self):
		'''Test check_syllables with poem_lines pattern and word_to_phonemes'''
		
		poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
		pattern = ([5, '7', 5], ['*', '*', '*'])
		word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],\
		'GAP': ['G', 'AE1', 'P'],\
		'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],\
		'LEADS': ['L', 'IY1', 'D', 'Z'],\
		'WITH': ['W', 'IH1', 'DH'],\
		'LINE': ['L', 'AY1', 'N'],\
		'THEN': ['DH', 'EH1', 'N'],\
		'THE': ['DH', 'AH0'], \
		'A': ['AH0'], \
		'FIRST': ['F', 'ER1', 'S', 'T'], \
		'ENDS': ['EH1', 'N', 'D', 'Z'],\
		'POEM': ['P', 'OW1', 'AH0', 'M'],\
		'OFF': ['AO1', 'F']}
		actual = check_syllables(poem_lines,pattern,word_to_phonemes)
		expected = ['With a gap before the next.']
		self.assertEqual(actual, expected)
	
	def test_not_all_require_checking(self):
		'''Test check_syllables with poem_lines pattern and word_to_phonemes'''
		
		poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
		pattern = ([5, 0, 5], ['*', '*', '*'])
		word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],\
		'GAP': ['G', 'AE1', 'P'],\
		'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],\
		'LEADS': ['L', 'IY1', 'D', 'Z'],\
		'WITH': ['W', 'IH1', 'DH'],\
		'LINE': ['L', 'AY1', 'N'],\
		'THEN': ['DH', 'EH1', 'N'],\
		'THE': ['DH', 'AH0'], \
		'A': ['AH0'], \
		'FIRST': ['F', 'ER1', 'S', 'T'], \
		'ENDS': ['EH1', 'N', 'D', 'Z'],\
		'POEM': ['P', 'OW1', 'AH0', 'M'],\
		'OFF': ['AO1', 'F']}
		actual = check_syllables(poem_lines,pattern,word_to_phonemes)
		expected = []
		self.assertEqual(actual, expected)
		
	
if __name__ == '__main__':
	unittest.main(exit=False)
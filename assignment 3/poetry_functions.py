"""
A poetry pattern:  tuple of (list of int, list of str)
  - first item is a list of the number of syllables required in each line
  - second item is a list describing the rhyme scheme rule for each line
"""

"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""

# ===================== Helper Functions =====================

def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to uppercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Birthday!!!')
    'BIRTHDAY'
    >>> clean_up('"Quoted?"')
    'QUOTED'
    """

    punctuation = """!"'`@$%^&_-+={}|\\/,;:.-?)([]<>*#\n\t\r"""
    result = s.upper().strip(punctuation)
    return result


def seperate(original, separators): #Taras Zelenenkyy A2 code
	result = []
	start = 0
	end = 0
	if len(separators)< 1 or len(original) < 1 : #check if empty
		return [original]
	for ch in original:
		if ch in separators:
			start = end #start separating where left off last loop
			end = original.find(ch) #find separator location
			if original[start:end] != '' and original[start:end] != ' ': 
				result.append(clean_up(original[start:end])) #add clean version
			original = original[:original.find(ch) ] + \
			original[original.find(ch) +1: ] #cut out separator
	if end < len(original): #if left over
		for ch in original[end:]:
			if ch != ' ': #if found non empty character = valid chunk
				result.append(clean_up(original[end:])) #add the rest
				return result # stop the loop and return
	return result


# ===================== Required Functions =====================

def count_lines(lst):
	r""" (list of str) -> int

	Precondition: each str in lst[:-1] ends in \n.

	Return the number of non-blank, non-empty strings in lst.

	>>> count_lines(['The first line leads off,\n', '\n', '  \n',
	... 'With a gap before the next.\n', 'Then the poem ends.\n'])
	3
	"""
	count = 0
	for line in lst:
		line = line.strip()
		if len(line)> 0:
			count += 1
	return count


def get_poem_lines(poem):
	r""" (str) -> list of str

	Return the non-blank, non-empty lines of poem, with whitespace removed 
	from the beginning and end of each line.

	>>> get_poem_lines('The first line leads off,\n\n\n'
	... + 'With a gap before the next.\nThen the poem ends.\n')
	['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
	"""
	lines = []
	temp = ''
	start = 0
	i = 0
	while i < len(poem):
		if poem[i] == '\n':
			temp = poem[start:i].strip() #start and end(i) cutting
			if len(temp) > 0: #non empty
				lines.append(temp)
			start = i #start capturing next chunk
		i+=1
	return lines


def check_syllables(poem_lines, pattern, word_to_phonemes):
	r""" (list of str, poetry pattern, pronunciation dictionary) -> list of str

	Precondition: len(poem_lines) == len(pattern[0])

	Return a list of lines from poem_lines that do not have the right number of
	syllables for the poetry pattern according to the pronunciation dictionary.
	If all lines have the right number of syllables, return the empty list.

	>>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
	>>> pattern = ([5, 5, 4], ['*', '*', '*'])
	>>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
	...                     'GAP': ['G', 'AE1', 'P'],
	...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
	...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
	...                     'WITH': ['W', 'IH1', 'DH'],
	...                     'LINE': ['L', 'AY1', 'N'],
	...                     'THEN': ['DH', 'EH1', 'N'],
	...                     'THE': ['DH', 'AH0'], 
	...                     'A': ['AH0'], 
	...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
	...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
	...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
	...                     'OFF': ['AO1', 'F']}
	>>> check_syllables(poem_lines, pattern, word_to_phonemes)
	['With a gap before the next.', 'Then the poem ends.']
	>>> poem_lines = ['The first line leads off,']
	>>> check_syllables(poem_lines, ([0], ['*']), word_to_phonemes)
	[]
	"""
	false_syllables = []
	line_num = 0
	for line in poem_lines:
		
		words = seperate(line, ' .,:;!?') #possible word separators
		count = 0
		if len(words) != 0 and pattern[0][line_num] != 0: #non empty 
														#and required to check
			for word in words:
				i=0
				while i <len(word_to_phonemes[word]): #checking 
													#every string in dictionary
					if word_to_phonemes[word][i][len(word_to_phonemes[word][i])\
					-1].isdigit(): #check if last character of string is number
						count += 1
					i+=1
			
			if count != pattern[0][line_num]: #match check
				false_syllables.append(line) #no match
		line_num +=1	
	return false_syllables

def check_rhyme_scheme(poem_lines, pattern, word_to_phonemes):
	r""" (list of str, poetry pattern, pronunciation dictionary) 
														-> list of list of str

    Precondition: len(poem_lines) == len(pattern[1])

    Return a list of lists of lines from poem_lines that should rhyme with 
    each other but don't. If all lines rhyme as they should, return the empty 
    list.

    >>> poem_lines = ['The first line leads off,', 'With a gap before the next.', 'Then the poem ends.']
    >>> pattern = ([5, 7, 5], ['A', 'B', 'A'])
    >>> word_to_phonemes = {'NEXT': ['N', 'EH1', 'K', 'S', 'T'],
    ...                     'GAP': ['G', 'AE1', 'P'],
    ...                     'BEFORE': ['B', 'IH0', 'F', 'AO1', 'R'],
    ...                     'LEADS': ['L', 'IY1', 'D', 'Z'],
    ...                     'WITH': ['W', 'IH1', 'DH'],
    ...                     'LINE': ['L', 'AY1', 'N'],
    ...                     'THEN': ['DH', 'EH1', 'N'],
    ...                     'THE': ['DH', 'AH0'], 
    ...                     'A': ['AH0'], 
    ...                     'FIRST': ['F', 'ER1', 'S', 'T'], 
    ...                     'ENDS': ['EH1', 'N', 'D', 'Z'],
    ...                     'POEM': ['P', 'OW1', 'AH0', 'M'],
    ...                     'OFF': ['AO1', 'F']}
    >>> check_rhyme_scheme(poem_lines, pattern, word_to_phonemes)
    [['The first line leads off,', 'Then the poem ends.']]
    """
	
	no_rhyme = []
	line_a = ''
	line_b = ''
	after_last_syllable = False
	i = 0 
	
	
	while i < len(poem_lines):# cycles through strings in list
		f = 0
		while f < len(poem_lines):# cycles through strings in list
			if pattern[1][i] == pattern[1][f] and f != i and pattern[1][i] != '*': 
				line_a = seperate(poem_lines[i], ' .,:;!?')#get words
				line_b = seperate(poem_lines[f], ' .,:;!?')#get words
				line_a = clean_up(line_a[len(line_a)-1])#get last word
				line_b = clean_up(line_b[len(line_b)-1])#get last word
				x = 0
				while x < len(word_to_phonemes[line_a]) and x < \
				len(word_to_phonemes[line_b]) and not after_last_syllable:
						#loops through strings in dictionary
					a = word_to_phonemes[line_a]\
					[len(word_to_phonemes[line_a])-1-x] #start at back
					b = word_to_phonemes[line_b]\
					[len(word_to_phonemes[line_b])-1-x] #start at back
					if a != b:
						temp = []
						z = 0
						while z < len(poem_lines):
							if pattern[1][z] == pattern[1][i]:
								temp.append(poem_lines[z]) #put 
							#all the lines with the same rhyme letter in temp
							z+=1
						if not temp in no_rhyme and len(temp) > 1:
							no_rhyme.append(temp) #temp is non empty and 
										   #not already in the non-rhyme section
					after_last_syllable =  a[len(a)-1].isdigit()\
					or b[len(b)-1].isdigit() #reached the last syllable,
											#no need to check further
					x+=1
			f+=1
		i+=1
	return no_rhyme


if __name__ == '__main__':
    import doctest
    doctest.testmod()

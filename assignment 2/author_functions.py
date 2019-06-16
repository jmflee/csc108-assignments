##########  Provided helper function. ############
def clean_up(s):
    """ (str) -> str

    Return a new string based on s in which all letters have been
    converted to lowercase and punctuation characters have been stripped
    from both ends. Inner punctuation is left untouched.

    >>> clean_up('Happy Birthday!!!')
    'happy birthday'
    >>> clean_up("-> It's on your left-hand side.")
    " it's on your left-hand side"
    """

    punctuation = "!',;:.-?)([]<>*#\n\t\r\""
    result = s.lower().strip(punctuation)
    return result

def remove_blank(word):
    """(list of str) -> (list of str)

    Returns the list word without blank elements consisting of "" or spaces

    >>> remove_blank(["food", "", "orange", ""])
    ["food", "orange"]
    """
    new_word = []
    for fragment in word:
        if not (fragment.replace(" ", "") == ''):
            new_word.append(fragment)
    return new_word

def word_concat(text):
    """(list of str) --> str

    Returns a sentence that is a concatenation of all the text in a list

    >>> word_concat(['food particles', 'orange particles'])
    " food particles orange particles"
    >>> word_concat(['%6wholesome goodness', 'in west side'])
    " %6wholesome goodness in west side"
    """
    new_word = ""
    for line in text:
        if(line[0] == " "):
            new_word = new_word + line
        else:
            new_word = new_word + line + " "
    return new_word

def pure_words(sentence):
    """ (str) -> list of str

    Return a list of strings based on a sentence in which all punctuation in each word is removed
    Inner punctuation is left intact

    >>> pure_words('Happy Birthday!!!')
    ['happy', 'birthday']
    >>> pure_words("-> It's on your left-hand side.")
    ["it's", 'on', 'your', 'left-hand', 'side']
    """
    fragments = remove_blank(sentence.split())
    result = []
    for words in fragments:
        result.append(clean_up(words))
    result = remove_blank(result)
    return result

def unique_words(sentence):
    """(list of str) -> dict of int

    Returns a dict of ints based on the number of occurrences of a word in sentence

    >>> unique_words(["oranges", "sweer", "potatoes", "oranges"])
    {"oranges": 2, "sweer": 1, "potatoes": 1}
    """
    instances = {}
    for word in sentence:
        if (word not in instances):
            instances[word] = 1
        else:
            instances[word] += 1
    return instances

##########  Complete the following functions. ############
def avg_word_length(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the average length of all words in text.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul and Mary\n']
    >>> avg_word_length(text)
    5.142857142857143
    """
    sum = 0
    counter = 0
    all_words = pure_words(word_concat(text))
    for word in all_words:
        sum = sum + len(word)
        counter += 1
    average = sum/counter
    return average

def type_token_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the Type Token Ratio (TTR) for this text. TTR is the number of
    different words divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n', 'James Gosling\n']
    >>> type_token_ratio(text)
    0.8888888888888888
    """
    new_words = pure_words(word_concat(text))
    result = len(unique_words(new_words)) / len(new_words)
    return result

def hapax_legomena_ratio(text):
    """ (list of str) -> float

    Precondition: text is non-empty. Each str in text ends with \n and
    text contains at least one word.

    Return the hapax legomena ratio for text. This ratio is the number of
    words that occur exactly once divided by the total number of words.

    >>> text = ['James Fennimore Cooper\n', 'Peter, Paul, and Mary\n', 'James Gosling\n']
    >>> hapax_legomena_ratio(text)
    0.7777777777777778
    """
    singles = 0
    sum = 0
    all_words = unique_words(pure_words(word_concat(text)))
    for words in all_words:
        if (all_words[words] == 1):
            singles +=1
        sum = sum + all_words[words]
    result = singles / sum
    return result

def split_on_separators(original, separators):
    """ (str, str) -> list of str

    Return a list of non-empty, non-blank strings from original,
    determined by splitting original on any of the separators.
    separators is a string of single-character separators.

    >>> split_on_separators("Hooray, Finally, we're done.", "!,")
    ['Hooray', ' Finally', " we're done."]
    """
    result = [""]
    location = 0
    for char in original:
        if (char in separators): #Creates new element if a seperator is contained
            result.append("")
            location += 1
        else:
            result[location] = result[location] + char
    result = remove_blank(result)
    return result

def avg_sentence_length(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.

    Return the average number of words per sentence in text.

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_length(text)
    17.5
    """
    paragraph = split_on_separators(clean_up(word_concat(text).strip()), ".!?")
    word_sum = 0
    for sentence in paragraph:
        word_sum = word_sum + len(pure_words(sentence))
    result = word_sum / len(paragraph)
    return result

def avg_sentence_complexity(text):
    """ (list of str) -> float

    Precondition: text contains at least one sentence.

    A sentence is defined as a non-empty string of non-terminating
    punctuation surrounded by terminating punctuation or beginning or
    end of file. Terminating punctuation is defined as !?.
    Phrases are substrings of sentences, separated by one or more of ,;:

    Return the average number of phrases per sentence in text.

    >>> text = ['The time has come, the Walrus said\n',
         'To talk of many things: of shoes - and ships - and sealing wax,\n',
         'Of cabbages; and kings.\n',
         'And why the sea is boiling hot;\n',
         'and whether pigs have wings.\n']
    >>> avg_sentence_complexity(text)
    3.5
    """
    paragraph = split_on_separators(clean_up(word_concat(text).strip()), ".!?")
    phrase_sum = 0
    for sentence in paragraph:
        phrase_sum = phrase_sum + len(split_on_separators(clean_up(word_concat(sentence).strip()), ",;:"))
    result = phrase_sum / len(paragraph)
    return result

def compare_signatures(sig1, sig2, weight):
    """ (list, list, list of float) -> float

    Return a non-negative float indicating the similarity of the two
    linguistic signatures, sig1 and sig2. The smaller the number the more
    similar the signatures. Zero indicates identical signatures.

    sig1 and sig2 are 6-item lists with the following items:
    0  : Author Name (a string)
    1  : Average Word Length (float)
    2  : Type Token Ratio (float)
    3  : Hapax Legomena Ratio (float)
    4  : Average Sentence Length (float)
    5  : Average Sentence Complexity (float)

    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.

    >>> sig1 = ["a_string" , 4.4, 0.1, 0.05, 10.0, 2.0]
    >>> sig2 = ["a_string2", 4.3, 0.1, 0.04, 16.0, 4.0]
    >>> weight = [0, 11.0, 33.0, 50.0, 0.4, 4.0]
    >>> compare_signatures(sig1, sig2, weight)
    12.000000000000007
    """
    sum = 0
    for type in range(1, 6):
        sum = sum + (abs(sig1[type] - sig2[type]) * weight[type])
    return sum
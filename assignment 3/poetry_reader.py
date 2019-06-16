"""
A pronunciation dictionary: dict of {str: list of str}
  - each key is a word (a str)
  - each value is a list of phonemes for that word (a list of str)
"""


def read_pronunciation(pronunciation_file):
    """ (file open for reading) -> pronunciation dictionary

    Read pronunciation_file, which is in the format of the CMU Pronouncing
    Dictionary, and return the pronunciation dictionary.
    """
    result = {}
    for line in pronunciation_file:
        if not (line[0] == ";;;"):
            word = line.strip().upper().split()
            result[word[0]] = word[1:len(word)]
    return result

def read_poetry_form_description(poetry_forms_file):
    """ (file open for reading) -> poetry pattern

    Precondition: we have just read a poetry form name from poetry_forms_file.

    Return the next poetry pattern from poetry_forms_file.
    """
    not_end = True
    syllables = []
    schemes = []
    info = []
    line = ''
    while not_end:
        line = poetry_forms_file.readline().strip()
        if line == '':
            not_end = False
        else:
            info = line.split()
            syllables.append(int(info[0]))
            schemes.append(info[1])
    result = (syllables, schemes)
    return result

def read_poetry_form_descriptions(poetry_forms_file):
    """ (file open for reading) -> dict of {str: poetry pattern}

    Return a dictionary of poetry form name to poetry pattern for the
    poetry forms in poetry_forms_file.
    """
    result = {}
    name = poetry_forms_file.readline().strip()
    while name:
        result[name] = read_poetry_form_description(poetry_forms_file)
        name = poetry_forms_file.readline().strip()
    return result
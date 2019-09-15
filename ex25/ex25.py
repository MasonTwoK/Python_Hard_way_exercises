'''
def break_words(stuff):
    """This function will break up words for us."""
    word = stuff.split(' ')
    return word

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
'''


def break_to_words(sent):
    words = sent.rsplit()
    return words

def sorted_words(words):
    word_in_order = sorted(words)
    return word_in_order

def print_first_word(words):
    first_word = words.pop(0)
    print("First word: ", first_word)

def print_last_word(words):
    last_word = words.pop(-1)
    print("Last word: {}".format(last_word))

def print_first_and_last(sentence):
    words = break_to_words(sentence)
    first = words.pop(0)
    last = words.pop(-1)
    print("First: {}\n Last: {}".format(first,last))

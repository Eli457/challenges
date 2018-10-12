from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    file = open('dictionary.txt')
    l = []

    for line in file:
        l.append(line.strip())

    file.close()
    return l


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    total = 0

    for l in word.upper():
        if l in LETTER_SCORES:
            total += LETTER_SCORES[l]

    return total


def max_word_value(list):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    

    pass


if __name__ == "__main__":
    #pass# run unittests to validate
    load_words()
    print(calc_word_value('Hello'))



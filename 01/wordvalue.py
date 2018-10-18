from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    file = open('dictionary.txt')
    d_list = []

    for line in file:
        d_list.append(line.strip())

    file.close()
    return d_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    total = 0

    for l in word.upper():
        if l in LETTER_SCORES:
            total += LETTER_SCORES[l]

    return total


def max_word_value(u_list=load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    max = calc_word_value(u_list[0])
    r_word = u_list[0]

    for word in u_list:
        if calc_word_value(word) > max:
            max = calc_word_value(word)
            r_word = word

    return r_word


if __name__ == "__main__":
    #pass# run unittests to validate
    load_words()
    print(calc_word_value('Hello'))
    print(max_word_value())



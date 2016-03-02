import string

def strip_line(line):
    """
    Removes all punctuation from a line of text.
    Returns a list of words.
    """
    return [x.strip(string.punctuation) for x in line.split()]


def get_all_words(lines):
    words = []
    for line in lines:
        words.extend(strip_line(line.lower())) # Best place for .lower()?
    return words


def count_words(words):
    count_dict = {}
    for word in set(words):
        count_dict[word] = words.count(word)
    return count_dict



with open("sample.txt") as text:
    lines = text.readlines()



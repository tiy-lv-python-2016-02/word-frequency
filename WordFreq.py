import string

def strip_line(line):
    """
    Removes all punctuation from a line of text.
    Returns a list of words.
    """
    return [x.strip(string.punctuation) for x in line.split()]


def get_all_words(lines):
    """
    :param lines: Multiple lines of stripped text.
    :return: Single list of lowered words.
    """
    words = []
    for line in lines:
        words.extend(strip_line(line.lower()))  # Best place for .lower()?
    return words


def count_words(words):
    """
    :param words: A list of lowered words to be counted
    :return: Dictionary of word counts
    """
    count_dict = {}
    for word in set(words):
        count_dict[word] = words.count(word)
    return count_dict


def top_counts(count_dict, number=20):

    top = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    for item in top[:number]:
        print(item[0], item[1])


if __name__ == '__main__':

    with open("sample.txt") as text:
        lines = text.readlines()



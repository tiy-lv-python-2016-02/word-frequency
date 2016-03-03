import string


def strip_line(line):
    """
    Removes all punctuation from a line of text

    :return: A list of words
    """
    return [x.strip(string.punctuation) for x in line.split()]


def get_all_words(lines):
    """
    :param lines: Multiple lines of stripped text
    :return: Single list of lowered words
    """
    words = []
    for line in lines:
        words.extend(strip_line(line.lower()))
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
    """
    Prints out the number of most frequent words

    :param count_dict: Dict of word frequencies
    :param number: Number of results to print
    """
    top = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    for item in top[:number]:
        print(item[0], item[1])


def main(lines):
    """
    Pulls everything into one nice function

    :return: Final result
    """
    words = get_all_words(lines)
    count_dict = count_words(words)
    return top_counts(count_dict)


if __name__ == '__main__':

    with open("sample.txt") as text:
        lines = text.readlines()

    main(lines)

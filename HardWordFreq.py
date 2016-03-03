import sys

from WordFreq import get_all_words, count_words


def clean_ignore(ignore):
    """
    :param ignore: Lines from a file of words to ignore
    :return: A list of individual ignore words
    """
    new_list = []
    for line in ignore:
        new_list.extend(line.split(","))
    return new_list


def histogram_print(count_dict, number=20):
    """
    Space variable is to keep formatting straight.

    :param count_dict: A dict of words counts
    :param number: How many results to print
    :return: Print a histogram of word frequencies
    """
    # reason for space
    most_occurrences = max(count_dict.values())
    if most_occurrences > 50:
        ratio = 50 / most_occurrences
        for word in count_dict:
            count_dict[word] = int(count_dict[word] * ratio + 0.5)
    top = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)[:20]
    for word in top:
        space = max([len(x[0]) for x in top])
        print(word[0].ljust(space), "#" * word[1])


def main_histogram(lines, ignored):
    """
    Main program that is called at end of file

    :param lines: Lines from file being counted
    :param ignored: Words to ignore
    :return: Print histogram of word frequencies
    """
    words = get_all_words(lines)
    words = [x for x in words if x not in ignored]
    count_dict = count_words(words)
    return histogram_print(count_dict)


if __name__ == '__main__':

    # Opens file with words to ignore
    with open("ignore.txt") as ignore_words:
        ignore = ignore_words.readlines()

    ignored = clean_ignore(ignore)

    # File to count, input on the command line
    file_to_read = sys.argv[-1]

    with open(file_to_read) as text:
        lines = text.readlines()

    main_histogram(lines, ignored)


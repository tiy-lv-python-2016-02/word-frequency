# Input file on command line
# Create hist
import string

from WordFreq import get_all_words, count_words, top_counts
# Top counts not needed after testing

def clean_ignore(ignore):
    new_list = []
    for line in ignore:
        new_list.extend(line.split(","))
    return new_list


def histogram_print(count_dict):
    pass


def main_histogram(lines, ignored):
    words = get_all_words(lines)
    words = [x for x in words if x not in ignored]
    count_dict = count_words(words)
    return top_counts(count_dict)




with open("ignore.txt") as ignore_words:
    ignore = ignore_words.readlines()

with open("sample.txt") as text:
    lines = text.readlines()[:20]

cleaned = clean_ignore(ignore)

main_histogram(lines, cleaned)


# Input file on command line
# Create hist

import string  # Unnecesary?

from WordFreq import get_all_words, count_words, top_counts
# Top counts not needed after testing

def clean_ignore(ignore):
    new_list = []
    for line in ignore:
        new_list.extend(line.split(","))
    return new_list


def histogram_print(count_dict, number=20):
    # If max > 50, scale = 50 / max
    # Convert dict values
    # Sorted and print
    most_occurrences = max(count_dict.values())
    if most_occurrences > 50:
        ratio = 50 / most_occurrences
        for word in count_dict:
            count_dict[word] = int(count_dict[word] * ratio + 0.5)
    top = sorted(count_dict.items(), key=lambda x: x[1], reverse=True)
    for word in top[:number]:
        print("#" * top[word])


def main_histogram(lines, ignored):
    words = get_all_words(lines)
    words = [x for x in words if x not in ignored]
    count_dict = count_words(words)
    return histogram_print(count_dict)




with open("ignore.txt") as ignore_words:
    ignore = ignore_words.readlines()

with open("sample.txt") as text:
    lines = text.readlines()[:20]

ignored = clean_ignore(ignore)

#main_histogram(lines, cleaned)

words = get_all_words(lines)
words = [x for x in words if x not in ignored]
count_dict = count_words(words)

from re import sub
from collections import Counter

if __name__ == '__main__':
    with open("sample.txt") as file:
        lines = file.readlines()

    words_from_text = []

    for line in lines:
        words = line.split()
        for word in words:
            word = sub('[^0-9a-zA-Z]+', '', word).lower()
            words_from_text.append(word)

    freq = Counter(words_from_text)

    top_words = freq.most_common(20)

    for key, value in top_words:
        print("{}: {}".format(key, value))
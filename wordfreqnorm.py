from re import sub
from collections import Counter


# def word_counter(text):
# freq = {}
# frequency is an empty dictionary
# going to be storing words as the key
# and number of times they pop up by their value


# def word_counter(text):
    # freq = {}

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

# s = re.sub('[^0-9a-zA-Z]+', '*', s)
# uses the sub function from the re library
# won't need re because we imported sub itself from re
# all non characters will be replaced with second argument
# on the third argument, your string
# the result of this becomes your new variable (s in this case)


# Your program should open sample.txt and read in the entirety of its text.
# You'll need to normalize the text so that words in different cases are
# still the same word and so it's scrubbed of punctuation.
# Once you've done that, go through the text and find the number of times each word is used.

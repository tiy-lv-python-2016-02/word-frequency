def word_counter(frequency, number=20):
    top_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    for item in top_words[:number]:
        print(item[0], item[1])

if __name__ == '__main__':

    file = open("sample.txt")

    lines = file.readlines() # this makes a string of the files from the text file

    freq = {}

    for line in lines:
        line = line.lower().replace(".", "").replace("'", "").replace(",", "").replace('"', '').replace("-", "")  # this removes capital letters and punctuation from the string
        words = line.split() # this splits the lines into individual words
        for word in words:
            freq[word] = freq.get(word, 0) + 1

    word_counter(freq)

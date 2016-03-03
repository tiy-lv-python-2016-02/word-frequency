from re import sub
from collections import Counter
import sys


if __name__ == '__main__':

    common_words = """
        a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
        because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
        for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
        it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
        not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
        since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
        twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
        would,yet,you,your
                   """
    common_words = common_words.replace(" ", "").replace("\n", "").split(",")

    required_file = sys.argv[-1]

    with open("sample.txt") as required_file:
        lines = required_file.readlines()

    words_from_text = []

    for line in lines:
        words = line.split()
        for word in words:
            word = sub('[^0-9a-zA-Z]+', '', word).lower()
            if word not in common_words:
                words_from_text.append(word)

    top_words = Counter(words_from_text).most_common(20)

    tags = "#"

    for key, value in top_words:
        print("{}: {}".format(key, tags*int((round(value) / 10))))
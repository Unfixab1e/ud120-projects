#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    if len(content) > 1:

        text_string = content[1].translate(string.maketrans("", ""), string.punctuation)        
    stemmer = SnowballStemmer("english")

    st = ""
    for word in text_string.split():
        st = st+" "+(stemmer.stem(word))

    words = st.lstrip()

    return words

    

def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()


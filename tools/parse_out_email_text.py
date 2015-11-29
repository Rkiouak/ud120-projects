#!/usr/bin/python

from nltk.stem.snowball import SnowballStemmer
import string

def parseOutText(f):
    """ given an opened email file f, parse out all text below the
        metadata block at the top
        (in Part 2, you will also add stemming capabilities)
        and return a string that contains all the words
        in the email (space-separated)

        example use case:
        f = open("email_file_name.txt", "r")
        text = parseOutText(f)

        """


    f.seek(0)  ### go back to beginning of file (annoying)
    all_text = f.read()

    ### split off metadata
    content = all_text.split("X-FileName:")
    words = ""
    counter=0
    if len(content) > 1:

        #Non obvious that the quiz wants the doublespaces/empty punctuation points replaced with single spaces
        content[1]=content[1].replace("  ", " ").replace("\n", " ")
        content=str(content[1]).split()
        stemmer = SnowballStemmer("english")
        for i in range(0, len(content)):
            ### remove punctuation and stem
            content[i]=content[i].translate(string.maketrans("", ""), string.punctuation)
            if len(stemmer.stem(content[i].replace(" ", "")).strip()) > 0:
                words += stemmer.stem(content[i].replace(" ", "")).replace("  ", "").strip()+" "

        ### project part 2: comment out the line below
        #words = text_string

        ### split the text string into individual words, stem each word,
        ### and append the stemmed word to words (make sure there's a single
        ### space between each stemmed word)





    return words



def main():
    ff = open("../text_learning/test_email.txt", "r")
    text = parseOutText(ff)
    print text



if __name__ == '__main__':
    main()

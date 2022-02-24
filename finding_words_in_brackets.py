"""
Functions finds all words in brackets
one function uses imported lib
one function uses a more manual approach
"""
import re
text = 'one two (three) four (fifty cent) six'

def findTextmanual(text, start, end):
    #manual
    words = []
    i = 0
    s = 0
    while i < len(text):
        if text[i] == start:
            s = i+1
        if text[i] == end:
            while s < i:
                words.append(text[s])
                s+=1
                if s == i:
                    words.append('\n')
        i+=1
    for i in range(len(words)):
        print(words[i],end ='')


def findText(text):
    #uses lib
    words = re.findall(r'\(.*?\)', text)
    for i in words:
        print("found brackets")
    return words

if __name__ == "__main__":
    print("Original text: "+ text)
    words = findText(text)
    print("Words in brackets: ",words)



"""
Functions Sort the words in order of their numeric value
"""

def manualsplitWords(text):
    #This function manually splits strings into seperate words without using libs
    words = []
    word = ''
    for i in text:
        if i == ' ':
            words.append(word)
            word = ''
        else:
            word += i
    if word:
        words.append(word)
    return words

def splitwords(text):
    #This function splits words using pythons inbuilt functions
    words = text.split()
    return words

def sortwords(text):
    #This function sorts words in length order from a list using the inbuilt sort method
    words = splitwords(text)
    print(words)
    words.sort(key=len)
    print(words)

def manualsortwords(text,sort):
    #This function sorts words by length without use of libs
    x = splitwords(text)
    n = len(text)
    for i in range(len(x) - 1):
        if sort == 'low':
            if len(x[i]) > len(x[i + 1]):
                x[i], x[i + 1] = x[i + 1], x[i]
        elif sort == 'high':
            if len(x[i]) < len(x[i + 1]):
                x[i], x[i + 1] = x[i + 1], x[i]
    print(x)

def sort(text):
    #This function combines the splitting and sorting functions functionality
    words = []
    word = ''
    for i in range(len(text)):
        if text[i] == ' ':
            words.append(word)
            word = ''
        else:
            word += text[i]
    if word:
        words.append(word)
    for i in range(len(words)-1):
        if len(words[i]) < len(words[i+1]):
            words[i], words[i+1] = words[i+1], words[i]
    print("sorted words ",words)

if __name__ == "__main__":
    string1 = 'twentyseven five twenty'
    string2 = 'twenty-one twenty-two thirteen seven six ten nineteen nine four fourteen'
    string3 = 'thirteen one four twenty thirty-four eight fifteen three thirty-five six thirty-six ten twenty-seven twenty-four thirty-one forty-seven thirty thirty-nine thirty-seven twenty-three forty-two two thirty-three thirty-eight twenty-five eleven seventeen twenty-one forty-nine forty-four zero forty-three twenty-six twelve twenty-nine seven twenty-eight eighteen five fourteen forty-six nine twenty-two forty-one sixteen forty-eight forty thirty-two forty-five nineteen'

    print("\nOriginal text: "+string1)
    sort(string1)

    print("\nOriginal text: " + string2)
    sort(string2)

    print("\nOriginal text: " + string3)
    sort(string3)
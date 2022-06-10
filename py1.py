import string
from random import randint

word = 'Hallowa keku'

def createstack():
    a = string.ascii_letters + string.digits + string.punctuation + ' '
    #print(a)
    return a

def broudforce(word):
    a = createstack()
    lenw = len(word)
    lena = len(a)
    forcedword = []
    for i in range(lenw):
        forcedword.append('#')
    for i in range(lenw):
        while word[i] != forcedword[i]:
            forcedword[i] = a[randint(0, lena - 1)]
            print(''.join(forcedword))
                
broudforce(word)
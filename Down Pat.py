import math

def pat(word):

    firstHalf = ''
    secondHalf = ''

    if len(word) == 1:
        print('YES')

    else:
        middle = math.ceil(len(word)/2)

        firstHalf = word[0:middle]
        secondHalf = word[middle::]

        
        if ord(firstHalf[0]) > ord(secondHalf[0]):
            print('YES')

        else:
            print('NO')


s1 = input('S1: ')
s2 = input('S2: ')
s1s2 = s1+s2

pat(s1)
pat(s2)
pat(s1s2)

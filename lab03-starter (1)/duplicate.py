'''
Write a program that accepts a sequence of whitespace separated words
as input and prints the words after removing all duplicate words and
sorting them alphanumerically. Suppose the following input is
supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Your program should take in only one line of input.

You may assume that your program will only be tested
with valid inputs.
'''

sentence = input()


# Define this function to return the expected output
# Do not print it from this function
def singlify(str):
    str = str.lower()
    list = str.split()
    retStr = ""
    BIGlist = []
    total = len(list)
    i = 0
    while i < total:
        if not (list[i] in BIGlist):
            BIGlist.append(list[i])
            retStr += list[i] + " "
        i += 1

    return retStr

print(singlify(sentence))

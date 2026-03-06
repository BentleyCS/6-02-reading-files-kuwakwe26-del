#You must make and submit your own test file and txt file with this assignment.

def toString(fileName):
    #This function returns the text from a given file.
    #Any new lines are written as \n
    f = open(fileName)
    out = ""
    for line in f:
        out += line
    return out
#print(toString("ExampleText.txt")=="Here is the text\ni am another line")

def longestLine(fileName):
    #Given a file return the longest line from within that file
    long =open(fileName,"r")
    long.readline()
    longest = ""
    for i in long:
        if len(i) > len(longest):
            longest = i
    return longest


def toBinary(fileName):
    #Given a file that is only 0's and 1's return a list of the file broken into bytes.
    #An example return might be ['01101001', '00101010', '1010']
    byte = open(fileName, "r")
    length = byte.read(8)
    binary = []
    while len(length) == 8:
        binary.append(length)
        length = byte.read(8)
        if len(length) != 8:
            binary.append(length)
    return binary


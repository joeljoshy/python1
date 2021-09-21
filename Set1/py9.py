f = open('word.txt', 'r')

lines = 0
words = 0
chars = 0
for line in f:

    line = line.strip('\n')
    print(line)
    lines +=1
    word = line.split()
    words+=len(word)
    chars += len(line)

f.close()
print("Number of lines : ",lines)
print("Number of words : ",words)
print("Number of characters : ",chars)
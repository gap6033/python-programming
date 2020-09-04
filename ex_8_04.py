#Open the file romeo.txt and read it line by line. For each line, split the line
#into a list of words using the split() method. The program should build a list
#of words. For each word on each line check to see if the word is already in the
#list and if not append it to the list. When the program completes, sort and
#print the resulting words in alphabetical order.

fname = input("Enter file name: ")
fhandle = open(fname)
ls = list()
for line in fhandle:#Read each line individually as a single string
    line = line.rstrip()
    words = line.split()#The string converted into a list, each word an item
    for i in range(len(words)):
        word = words[i]#Slices out the word from the list
        if word not in ls:
            ls.append(word)#sliced word if not duplicate added to the empty list
ls.sort()
print(ls)

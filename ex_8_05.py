
#Open the file mbox-short.txt and read it line by line. When you find a line that
#starts with 'From ' like the following line:
#'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
#You will parse the From line using split() and print out the second word in the
#line (i.e. the entire address of the person who sent the message). Then print
#out a count at the end.

fname = input("Enter file name: ")
fhandle = open(fname)
count = 0
for line in fhandle:
    if line.startswith('From '):#Notice the question had space after 'From '
        line = line.rstrip()
        line = line.split()
        count = count + 1
        print(line[1])
    else:# To make sure list index doesn't go out of range
        continue
print("There were", count, "lines in the file with From as the first word")

#You will read through and parse a file with text and numbers. You will extract
#all the numbers in the file and compute the sum of the numbers.
import re
fname = input("Enter file name: ")
fhandle = open(fname)

ls_1 = list()
for line in fhandle:
    ls = re.findall('[0-9]+', line) #you get multiple lists, one for each line, the lists contain no.s but in string format.
    for i in ls:#to loop over the no.s in a list individually and extract the number
        ls_1.append(float(i))#to append the extracted number in one single list and convert them into integers or float (either is fine)
print(sum(ls_1))

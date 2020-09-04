#Write a program to read through the mbox-short.txt and figure out who has sent
#the greatest number of mail messages. The program looks for 'From ' lines and
#takes the second word of those lines as the person who sent the mail. The
#program creates a Python dictionary that maps the sender's mail address to a
#count of the number of times they appear in the file. After the dictionary is
#produced, the program reads through the dictionary using a maximum loop to find
#the most prolific committer.
#The approach: open the file and read the lines one by one while simultaneously
#forming a 'list' of those lines which start with 'From ', slice the 2nd word from
#the line being looped and append it to a previously created constructor
#variable of type list.
    #After you've read through the entire file, you'll now
#have a list variable that would contain the 2nd word from each of the lines
#that started with 'From '. Read the words from this list and add it to the
#constructory variable of type dictionary; where the each word would be the 'key'
#and the no. of times it appears would be its 'value'
    #Now from the dictionary so created you need to extract the key-value pair
#which has the highest value.

count = dict()#constructor variable empty dictionary
words = list()#constructor variable empty list
fname = input("Enter file name: ")
fhandle = open(fname)

for line in fhandle:
    if line.startswith('From '):#looks for lines that start with 'From '
        line = line.split()#Convert the line satifying if condition into list
        words.append(line[1])#extracts 2nd word from the list and add it to the empty list variable
    else:
        continue#this is to make sure the loop doesn't run out of index

for person in words:#loop that goes through the list of '2nd words' created above
        count[person] = count.get(person,0) + 1#extracts word from the list and add it to the empty dictionary variable as key, with value being the number of times the word occurs

sender = None
max_mail = None
for k, v in count.items():# count.items() converted the dictionary into a tupple and allowed us to use two iteration variables, corresponding to the key-value pair
    if max_mail == None or v > max_mail:#this allows us to find highest value and its corresponding key
        sender = k
        max_mail = v
print(sender, max_mail)

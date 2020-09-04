#Write a program to read through the mbox-short.txt and figure out the
#distribution by hour of the day for each of the messages. You can pull the hour
#out from the 'From ' line by finding the time and then splitting the string a
#second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.

fname = input("Enter file name: ")
while fname != 'mbox-short.txt':
    fname = input("Enter valid file name: ")
    if fname == 'mbox-short.txt':
        break
fhandle = open(fname)

time = list()
hours = list()
for line in fhandle:
    if line.startswith('From '):
        line = line.split()
        time = line[5]
        hour = time[0:2]
        hours.append(hour)
    else:
        continue

count = dict()
for hour in hours:
    count[hour] = count.get(hour, 0) + 1

for key, val in sorted(count.items()):
    print(key, val)

#In this assignment you will write a Python program that expands on
#http://www.py4e.com/code3/urllinks.py. The program will use urllib to read the
#HTML from the data files below, extract the href= vaues from the anchor tags,
#scan for a tag that is in a particular position relative to the first name in
#the list, follow that link and repeat the process a number of times and report
#the last name you find.

#We provide two files for this assignment. One is a sample file where we give
#you the name for your testing and the other is the actual data you need to
#process for the assignment

#Sample problem: Start at http://py4e-data.dr-chuck.net/known_by_Fikret.html
#Find the link at position 3 (the first name is 1). Follow that link. Repeat
#this process 4 times. The answer is the last name that you retrieve.
#Sequence of names: Fikret Montgomery Mhairade Butchi Anayah
#Last name in sequence: Anayah

#Actual problem: Start at: http://py4e-data.dr-chuck.net/known_by_Katlyn.html
#Find the link at position 18 (the first name is 1). Follow that link. Repeat
#this process 7 times. The answer is the last name that you retrieve.


# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')
count = 0
for i in range(7):
    fhandle = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(fhandle, 'html.parser')
    tag = soup('a')[17]
    url = tag.get('href', None)
    content = tag.contents[0]
    count = count + 1
    print("URL No.: ", count)
    print("Retrieving URL: ", url)
    print("Name: ", content)

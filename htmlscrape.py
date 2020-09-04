#read the HTML from the data files below, and parse the data, extracting
# numbers and compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give
#you the sum for your testing and the other is the actual data you need to
#process for the assignment.
#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_293684.html (Sum ends with 37)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all that is within span tags
count = 0
sum = 0
tags = soup('span')
for tag in tags:
    number = int(tag.contents[0])
    sum = sum + number
    count = count + 1
print('Count: ', count)
print('Sum: ', sum)

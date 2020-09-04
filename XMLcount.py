# The program will prompt for a URL, read the XML data from that URL using urllib
# and then parse and extract the comment counts from the XML data, compute the sum
#  of the numbers in the file.
#
# We provide two files for this assignment. One is a sample file where we give you
# the sum for your testing and the other is the actual data you need to process for
# the assignment.
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.xml (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_293686.xml (Sum ends with 66)

import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Access the URL
url = input('Enter URL: ')
data = urllib.request.urlopen(url).read()

# Retrieving XML data from URL
stuff = ET.fromstring(data)
lst = stuff.findall('comments/comment')
ls = list()#
for item in lst:
    number = int(item.find('count').text)
    ls.append(number)

print(sum(ls))

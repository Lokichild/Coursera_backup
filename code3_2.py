# Initial imports
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defauts to certicate verification and most secure protocol (now TLS)

# Ignore SSL/TLS certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Set up starting parameters
url = input('Enter URL: ')
count = int(input('Enter count: '))
pos = int(input('Enter position: '))
pos = pos - 1
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve urls and iterate 'count' number of time at 'pos' position
while count > 0:
    tags = soup('a')
    tag = tags[pos]
    newurl = tag.get('href', None)
    print(newurl)
    html = urllib.request.urlopen(newurl, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    count = count - 1
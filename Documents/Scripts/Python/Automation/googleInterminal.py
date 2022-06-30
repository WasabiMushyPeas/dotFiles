#!/usr/bin//env python
import sys
from bs4 import BeautifulSoup
import urllib.request


#                                       Command Line Interface
searchTerms = [""]

for arg in sys.argv:
    searchTerms.append(arg)

linkifiedSearch = "https://www.google.com/search?q="

for x in range(2, len(searchTerms)):
    linkifiedSearch += searchTerms[x]


#                                       HTML requests
request = urllib.request.Request(linkifiedSearch)
request.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36')

raw_response = urllib.request.urlopen(request).read()
page = raw_response.decode("utf-8")



print(page)

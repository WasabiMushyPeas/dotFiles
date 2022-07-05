#!/usr/bin//env python
import sys
import os
#                                       Command Line Interface
searchTerms = [""]

for arg in sys.argv:
    searchTerms.append(arg)

linkifiedSearch = "https://www.google.com/search?q="

for x in range(2, len(searchTerms)):
    linkifiedSearch += searchTerms[x]

print("lynx " + linkifiedSearch + " -accept_all_cookies")
os.system("lynx " + linkifiedSearch + " -accept_all_cookies")

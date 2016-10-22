from bs4 import BeautifulSoup
import urllib
from lxml import html
import requests
import sys
import argparse

#args = get_args()                                                                                                                                                                                  
url = sys.argv[1]
response = requests.get(url)
soup = BeautifulSoup(response.text)
#print(soup.prettify())
for link in soup.find_all('a'):
    print(link.get('href'))




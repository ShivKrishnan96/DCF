from bs4 import BeautifulSoup
import urllib
from lxml import html
import requests
import sys
import argparse
from xlrd import open_workbook, XLRDError

def getFormNumber(s):
    l = s.split('-')
    if '.txt' in l[2]:
        l[2] = l[2].partition('.')[0]
    return (l[0]+l[1]+l[2],l[1])

def test_book(filename):
    try:
        open_workbook(filename)
    except XLRDError:
        return False
    else:
        return True

#args = get_args()
company = sys.argv[1]
comp = company.split('_')
#print comp                                                                                                                                                                                  
url1 = 'https://www.sec.gov/cgi-bin/srch-edgar?text=company-name%3D%22international+business+machines+corp%22+AND+form-type%3D%2810-k*%29&first=2011&last=2016'
url = 'https://www.sec.gov/cgi-bin/srch-edgar?text=company-name%3D%22'+comp[0].lower()
for i in range(1,len(comp)):
    url = url+'+'+comp[i].lower()
url = url + '%22+AND+form-type%3D%2810-k*%29&first=2011&last=2016'
print url
response = requests.get(url)
soup = BeautifulSoup(response.text, "lxml")
#print(soup.prettify())
list1 = []
Accession_number= []
year = []
for link in soup.find_all('a'):
    if ('/Archives')  in (link.get('href')):
        v = link.get('href')
        list1.append(link.get('href'))
        x,y = getFormNumber(v.split('/')[6])
        Accession_number.append(x)
        year.append(y)

CIK = list1[0].split('/')[4]
Accession_number = list(set(Accession_number))
year = list(set(year))
year.sort()

Accession_number.sort()

for i in Accession_number:
    dls = 'https://www.sec.gov/Archives/edgar/data/' + CIK + '/' + i + '/Financial_Report.xlsx'

    

    


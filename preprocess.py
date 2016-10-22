from bs4 import BeautifulSoup
import urllib
from lxml import html
import requests
import sys
import argparse
from xlrd import open_workbook, XLRDError
from excel import createExcel
from DCF import Make_DCF


def getFormNumber(s):
    l = s.split('-')
    if '.txt' in l[2]:
        l[2] = l[2].partition('.')[0]
    return (l[0]+l[1]+l[2],l[1])

def preprocesser(company):

	comp = company.split('_')                                                                                                                                                                                  
	url = 'https://www.sec.gov/cgi-bin/srch-edgar?text=company-name%3D%22'+comp[0].lower()
	for i in range(1,len(comp)):
	    url = url+'+'+comp[i].lower()
	url = url + '%22+AND+form-type%3D%2810-k*%29&first=2013&last=2016'
	print url
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "lxml")
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

        file_names = []

        ctr = 0

	for i in range(3):
	    dls = 'https://www.sec.gov/Archives/edgar/data/' + CIK + '/' + Accession_number[len(Accession_number) - i - 1] + '/Financial_Report.xlsx'
	    if createExcel(dls, company+year[len(year) - i-1]+".xlsx"):
                ctr += 1
                file_names.append(company+year[len(year) - i-1]+".xlsx")

        if ctr == 3:
            Make_DCF(file_names)
        else:
            print "Not enough data to proceed"

def main():
    preprocesser(sys.argv[1])

            
if __name__ == "__main__":
    main()    

    


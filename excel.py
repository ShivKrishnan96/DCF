
import urllib
from xlrd import open_workbook, XLRDError
#dls = "https://www.sec.gov/Archives/edgar/data/51143/000104746916010329/Financial_Report.xlsx" 
#dlsWrong = "https://www.sec.gov/Archives/edgar/data/51143/$$$000104746916010329/Financial_Report.xlsx" 


def test_book(filename):
    try:
        open_workbook(filename)
    except XLRDError:
        return False
    else:
        return True

#create an excel file from url dls, save as nameOfFile
def createExcel(dls, nameOfFile):
    urllib.urlretrieve(dls, nameOfFile)

    if test_book(nameOfFile):
        print("success")
    else:
        print("fail")




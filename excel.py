
import urllib
from xlrd import open_workbook, XLRDError
dls = "https://www.sec.gov/Archives/edgar/data/51143/000104746916010329/Financial_Report.xlsx" 
dlsWrong = "https://www.sec.gov/Archives/edgar/data/51143/$$$000104746916010329/Financial_Report.xlsx" 

x = urllib.urlretrieve(dls, "myExcel.xls")

def test_book(filename):
    try:
        open_workbook(filename)
    except XLRDError:
        return False
    else:
        return True




if test_book("myExcel.xls"):
    print("success")
else:
    print("fail")

#    print("success")
#else:
#    print("failed")




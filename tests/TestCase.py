import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from xml.dom import minidom
import pages.SearchPage
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get('https://www.w3schools.com/html/html_tables.asp')
    request.cls.driver = driver
    yield driver
    driver.close()
@pytest.mark.usefixtures("setup")
class TestCase:
    def test_main(self):
        try:
             # try to open file xml
            file = minidom.parse('data.xml')
        except:
            #create base file xml
            root = minidom.Document()

            xml = root.createElement('data')
            root.appendChild(xml)

            productChild = root.createElement('searches')

            xml.appendChild(productChild)

            xml_str = root.toprettyxml(indent="\t")

            save_path_file = "data.xml"

            with open(save_path_file, "w") as f:
                f.write(xml_str)

            #Fetching from the website based on data on the XML page

        for i in range(len(file.getElementsByTagName('search'))):
            returnColumnText = file.getElementsByTagName('returnColumnText')[i].firstChild.data
            searchText=file.getElementsByTagName('searchText')[i].firstChild.data
            searchColum=file.getElementsByTagName('searchColumn')[i].firstChild.data
            expectedText=file.getElementsByTagName('expectedText')[i].firstChild.data
            #Creating an object of type SearchPage

            ps=pages.SearchPage.SearchPage()
              #Checking whether the incoming data is correct

            if(ps.verifyTableCellText(self.driver,searchColum,searchText,returnColumnText,expectedText)==True):
                 #Printing the correct data
                print(ps.getTableCellTextByXpath(self.driver,searchColum,searchText,returnColumnText))




from selenium.webdriver.common.by import By


class SearchPage:
    #function that checks whether the data returned from the web page matches the data that should have been returned

    def verifyTableCellText(self, table, searchColumn,
                            searchText, returnColumnText, expectedText):
        try:
            assert expectedText == self.getTableCellTextByXpath(table, searchColumn, searchText, returnColumnText)
            return True
        except:
            return False
    #function that retrieves data from web according to XPATH

    def getTableCellTextByXpath(self, table, searchColumn, searchText, returnColumnText):
        try:
            driver = table
            xpath = "//*[@id='customers']/tbody/tr[td='"+searchText+"']/td["+returnColumnText+"]"
            t = driver.find_element(By.XPATH, xpath)
            return t.text
        except:
            raise Exception

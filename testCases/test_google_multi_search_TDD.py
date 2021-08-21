from pageObjects.searchPage import SearchPage
from utilities import XLUtility
from utilities.XLUtility import readData, getRowCount
from utilities.logGeneration import LogGen
from utilities.readConfig import ReadConfig


class Test_002_google_multi_search:
    logger = LogGen.log()
    url = ReadConfig.get_application_url()
    path = '/home/manish/Documents/Programming/Python/pythonProject/google_Search_Automation_Framwork_Python/' \
           'Test_Data/test_data.xlsx'

    def test_google_multiSearch_method(self, setup):

        self.logger.info("testing Multi google search, test_google_multiSearch_method")
        self.driver = setup
        self.driver.get(self.url)
        self.logger.info("Invoking browser")

        self.logger.info("Initializing the search page object")
        self.sp = SearchPage(self.driver)
        self.logger.info("calling the test data from XL file")
        self.rows = XLUtility.getRowCount(self.path, "Sheet1")
        print(f"Number of rows in excel is {self.rows + 1}")
        test_status = []
        for row in range(2, self.rows + 1):
            searchtext = XLUtility.readData(self.path, "Sheet1", row, 1)
            exp = XLUtility.readData(self.path, "Sheet1", row, 2)
            self.sp.set_text_to_search(searchtext)
            title = self.driver.title
            if 'Search' in title:
                if exp == 'pass':
                    self.logger.info("Title matched")
                    test_status.append("pass")
                    assert True
                elif exp == 'fail':
                    self.logger.info("title match but expectation did not match")
                    test_status.append("fail")
                    assert False

            elif 'Search' not in title:
                if exp == 'pass':
                    self.logger.error("title did not match but it was expectation")
                    test_status.append("pass")
                    assert True
                elif exp == 'fail':
                    self.logger.error("title did not match and it was not the expectation")
                    test_status.append("fail")
                    assert False
        if 'fail' not in test_status:
            self.logger.info("*** test_google_multiSearch_method is passed ***")
            self.driver.close()
            assert True
        if 'fail' in test_status:
            self.logger.info("*** test_google_multiSearch_method is failed ***")
            self.driver.close()
            assert False

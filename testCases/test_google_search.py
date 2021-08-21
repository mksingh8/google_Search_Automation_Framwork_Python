from pageObjects.searchPage import SearchPage
from utilities.logGeneration import LogGen
from utilities.readConfig import ReadConfig


class Test_001_Google_Search:
    logger = LogGen.log()
    url = ReadConfig.get_application_url()

    def test_google_search_method(self, setup):
        self.logger.info("*** test_google_search_method ***")
        self.driver = setup
        self.driver.get(self.url)
        self.logger.info("Invoking browser")

        self.logger.info("Initializing the search page object")
        self.sp = SearchPage(self.driver)
        self.sp.set_text_to_search("red wine")

        if 'Search' in self.driver.title:
            self.logger.info("Title matched")
            assert True

        else:

            self.logger.error("title did not match")
            assert False

        self.driver.close()

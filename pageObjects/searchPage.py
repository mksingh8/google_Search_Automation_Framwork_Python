from selenium.webdriver.common.keys import Keys


class SearchPage:
    txt_box_search_name = 'q'
    btn_Googlesearch_name = 'btnK'

    def __init__(self, driver):
        self.driver = driver

    def set_text_to_search(self, text):
        self.driver.find_element_by_name(self.txt_box_search_name).send_keys(text, Keys.RETURN)

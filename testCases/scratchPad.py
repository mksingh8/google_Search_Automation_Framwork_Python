from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from utilities import XLUtility
from utilities.XLUtility import getRowCount
from utilities.logGeneration import LogGen


#
# class ScratchPad:
#     logger = LogGen.log()
#     path = '/home/manish/Documents/Programming/Python/pythonProject/google_Search_Automation_Framwork_Python' \
#            '/Test_Data/test_data.xlsx '
#
#     def log_check(self):
#         print("this is method in class scratchPad")
#         # self.logger.info("printing log message from another module")
#         print(getRowCount(self.path, "Sheet1"))
#
#
# if __name__ == '__main__':
#     sp = ScratchPad()
#     sp.log_check()
# path = '/home/manish/Documents/Programming/Python/pythonProject/google_Search_Automation_Framwork_Python/Test_Data' \
#        '/auto_test_data.xlsx '
# row = XLUtility.getRowCount(path, 'Sheet1')
# print(f"# of rows is {row}")

class A:
    def screenshottest(self):
        option = Options()
        option.add_argument('--no-sandbox')
        option.add_experimental_option('useAutomationExtension', False)
        # option.add_argument('--headless')
        # driver = webdriver.Chrome(ChromeDriverManager().install())
        driver = webdriver.Chrome(executable_path="/home/manish/Documents/browsers/chromedriver", options=option)
        driver.get("https://www.facebook.com")
        driver.save_screenshot("/home/manish/Documents/Programming/Python/pythonProject"
                               "/google_Search_Automation_Framwork_Python/Screenshots/" + __name__ + ".png")
        driver.close()



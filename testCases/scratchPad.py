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
path = '/home/manish/Documents/Programming/Python/pythonProject/google_Search_Automation_Framwork_Python/Test_Data' \
       '/auto_test_data.xlsx '
row = XLUtility.getRowCount(path, 'Sheet1')
print(f"# of rows is {row}")

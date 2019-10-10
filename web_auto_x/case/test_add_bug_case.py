from selenium import webdriver
import unittest
from pages.login_page import LoginPage
from  pages.add_bug_page import AddBugPage
import time

my="http://127.0.0.1/zentao/my/"

class AddBugCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.bug=AddBugPage(cls.driver)
        a=LoginPage(cls.driver)
        a.login()
        #cls.xx=XXPage(cls.driver)

    def setUp(self):
        #每个用例都在一个起点
        self.driver.get(my)


    def test_add_xxx(self):
         '''添加BUG'''
         timestr=time.strftime("%Y_%m_%d_%H_%M_%S")
         title="测试提交BUG"+timestr
         self.bug.add_bug(title)
         result=self.bug.is_add_bug_sucess(title)
         print(result)
         self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()
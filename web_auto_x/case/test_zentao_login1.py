#coding:utf-8

from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    '''登陆类的案例'''
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()

    def setUp(self):
        self.driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
        self.is_alter_exist()
        self.driver.delete_all_cookies()  #退出登录
        self.driver.refresh()

    def get_login_username(self):
        try:
            t=self.driver.find_element_by_css_selector("#userNav>li>a>span.user-name").text
            print(t)
            return t
        except:
            return ""


    def is_alter_exist(self):
        '''判断alter是不是在'''
        try:
            time.sleep(3)
            alter=self.driver.switch_to.alert
            text=alter.text
            alter.accept() #用alter 点alter
            return text
        except:
            return ""

    def login(self,user,paw):
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(paw)
        self.driver.find_element_by_id("submit").click()

    def test_01(self):
        '''登录成功的案例'''
        time.sleep(2)
        self.login("admin","Wln123456")
        #判断是否登录成功
        time.sleep(2)
        t=self.get_login_username()
        print("获取登陆的结果：%s"%t)
        self.assertTrue(t=="admin")

    def test_02(self):
        '''登录失败的案例'''
        time.sleep(2)
        #错误账号和密码
        self.login("admin1","")
        #判断是否登录成功
        time.sleep(2)
        t=self.get_login_username()
        print("登陆失败，获取结果：%s"%t)
        self.assertTrue(1==2) #断言失败截图

    # def tearDown(self):
    #     self.is_alter_exist()
    #     self.driver.delete_all_cookies() #清空cookies,退出登录
    #     self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit() #编辑器问题

    if __name__=="__main__":
        unittest.main()



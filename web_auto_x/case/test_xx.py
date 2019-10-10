from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
'''
1.输入admin，输入Wln123456 点击登录 期望结果
2.输入admin，不输入密码 点击登录
3.输入admin，输入Wln123456 点击记住密码 点击登录
4.点击忘记密码
'''
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginp=LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.loginp.is_alter_exist()
        self.driver.delete_all_cookies()  #退出登录
        self.driver.refresh()

    def test_01(self):
        '''输入账号admin，输入密码Wln123456 点击登录'''
        self.loginp.input_user("admin")
        self.loginp.input_psw("Wln123456")
        self.loginp.click_login_button()
        result=self.loginp.get_login_name()
        self.assertTrue(result=="admin")

    def test_02(self):
        '''输入admin，不输入密码 点击登录'''
        self.loginp.input_user("admin")
        self.loginp.click_login_button()
        result=self.loginp.get_login_name()
        self.assertTrue(result=="")

    def test_03(self):
        '''输入admin，输入Wln123456 点击记住密码 点击登录'''
        self.loginp.input_user("admin")
        self.loginp.input_psw("Wln123456")
        self.loginp.click_keep_login()
        self.loginp.click_login_button()
        result=self.loginp.get_login_name()
        self.assertTrue(result=="admin")

    def test_04(self):
        '''点击忘记密码'''
        self.loginp.click_forget_psw()
        result=self.loginp.is_refresh_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()
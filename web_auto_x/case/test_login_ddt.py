from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import ddt
from common.read_excel import ExceUtil
import os
'''
1.输入admin，输入Wln123456 点击登录 期望结果
2.输入admin，不输入密码 点击登录
3.输入admin111，输入Wln123456 点击登录
'''

#测试的数据
testdates=[
    {"user":"admin","psw":"Wln123456","expect":True},
    {"user":"admin","psw":"","expect":False},
    {"user":"admin111","psw":"Wln123456","expect":False},
]

# propath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# filepath=os.path.join(propath,"common","datas.xls")
# print(filepath)
# data=ExceUtil(filepath)
# testdates=data.dict_data()
# print(testdates)

@ddt.ddt
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Firefox()
        cls.loginp=LoginPage(cls.driver)
        cls.driver.get(login_url)

    def setUp(self):
        self.loginp.is_alter_exist()
        self.driver.delete_all_cookies()  #退出登录
        self.driver.refresh()
        self.driver.get(login_url)



    def login_case(self,user,psw,expect):
        self.loginp.login(user,psw)
        # self.loginp.input_user(user)
        # self.loginp.input_psw(psw)
        # self.loginp.click_login_button()
        result=self.loginp.get_login_result(user)
        print("测试结果：%s" %result)
        self.assertTrue(result==expect)

    # @ddt.data({"user":"admin","psw":"Wln123456","expect":"admin"},
    #          {"user":"admin","psw":"","expect":""},
    #          {"user":"admin111","psw":"Wln123456","expect":""},)
    @ddt.data(*testdates)
    def test_01(self,data):
        '''输入账号admin，输入密码Wln123456 点击登录'''
        print("-------------------开始测试------------------------")
        print("测试数据 %s"%data)
        self.login_case(data["user"],data["psw"],data["expect"])
        print("-------------------结束：pass!------------------------")

    # def test_02(self):
    #     '''输入admin，不输入密码 点击登录'''
    #     print("-------------------开始测试：test_02------------------------")
    #     data2=testdates[1]
    #     print("测试数据 %s"%data2)
    #     self.login_case(data2["user"],data2["psw"],data2["expect"])
    #     print("-------------------结束：pass!------------------------")
    #
    # def test_03(self):
    #     '''输入admin111，输入Wln123456 点击记住密码 点击登录'''
    #     print("-------------------开始测试：test_03------------------------")
    #     data3=testdates[2]
    #     print("测试数据 %s"%data3)
    #     self.login_case(data3["user"],data3["psw"],data3["expect"])
    #     print("-------------------结束：pass!------------------------")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main()
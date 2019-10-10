from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class Base():
    '''基于原生selenium做二次封装'''

    def __init__(self,driver:webdriver.Firefox):
        self.driver=driver
        self.timeout=10
        self.t=0.5

    def findElementNew(self,locator):
        '''定位到元素，返回元素对象，没定位到元素，Timeout异常'''
        ele=WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_all_elements_located(locator))
        return ele

    def findElement(self,locator):
        if not isinstance(locator,tuple):
            print('locator参数类型错误，必须传元祖类型：loc=("id","value1")')
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s"%(locator[0],locator[1]))
            ele=WebDriverWait(self.driver,self.timeout,self.t).until(lambda x: x.find_element(*locator))
            return ele

    def findElements(self,locator):
        try:
            eles=WebDriverWait(self.driver,self.timeout,self.t).untils(lambda x: x.find_element(*locator))
            return eles
        except:
            return []

    def sendKeys(self,locator,text):
        ele =self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
         ele =self.findElement(locator)
         ele.click()

    def clear(self,locator):
        ele=self.findElement(locator)
        ele.clean()

    def isSelected(self,locator):
        '''判断元素是否被选中，返回bool值'''
        ele=self.findElement(locator)
        r=ele.is_selected()
        return r

    def isElementExist(self,locator):
        try:
            ele=self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self,locator):
        eles=self.findElement(locator)
        n=len(eles)
        if n==0:
            return False
        elif n==1:
            return True
        else:
            print("定位到元素个数:%s"%n)
            return True

    def is_title(self,_title):
        '''返回bool值 '''
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self,_title):
        '''返回bool值 '''
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    #def is_text_to_be_present_in_element(self,locator,_text):
    def is_text_in_element(self,locator,_text):
        '''返回bool值 '''
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_value_in_element(self,locator,_value):
        '''返回bool值,value为空字符串，返回False '''
        try:
            result=WebDriverWait(self.driver,self.timeout,self.t).until(EC.text_to_be_present_in_element_value(locator,_value))
            return result
        except:
            return False

    def is_alter(self):
        try:
            result=WebDriverWait(self.driver,3,self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        '''获取title'''
        return self.driver.title

    def get_text(self,locator):
        '''获取文本'''
        try:
            t=self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回''")
            return ""

    def switch_handle(self,window_name):
        self.driver.switch_to_window(window_name)

    def switch_alter(self):
        r=self.is_alter()
        if not r:
            print("alter不存在")
        else:
            return r

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        ele=self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()

    def js_focus_element(self,locator):
        '''聚焦元素'''
        target=self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target)

    def ja_scroll_top(self):
        '''滚动到顶部'''
        js="window.scrollTo(0.0)"
        self.driver.execute_script(js)

    def js_scroll_end(self,x=0):
        '''滚动到底部'''
        js="window.scrollTo(%s,document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select_by_index(self,locator,index=0):
        '''通过索引，index是索引第几个，从0开始，默认选择第一个'''
        element=self.findElement(locator)
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        '''通过value属性'''
        element=self.findElement(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        '''通过文本值定位'''
        element=self.findElement(locator)
        Select(element).select_by_visible_text(text)


if __name__=="__main__":
    driver=webdriver.Firefox()
    driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
    zentao=Base(driver)
    # loc1=(By.ID,"account")
    # loc2=(By.CSS_SELECTOR,"[name='password']")
    # loc3=(By.XPATH,"//*[@id='submit']")

    loc1=("id","account")
    loc2=("css selector","[name='password']")
    loc3=("xpath","//*[@id='submit']")

    zentao.sendKeys(loc1,"admin")
    zentao.sendKeys(loc2,"Wln123456")
    zentao.click(loc3)

    zentao


    # driver.switch_to_frame("xxx")
    # zentao.sendKeys(loc1,"admin")
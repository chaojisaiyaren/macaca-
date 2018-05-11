import time
from macaca import WebDriverException
from conf.decorator import teststep, teststeps
from conf.basepage import BasePage
import re

class HomePage(BasePage):
    """主界面"""

    @teststeps
    def my_self(self):
        """点击我进入微信的个人界面 """
        self.driver.element_by_name("我").click()

    @teststeps
    def my_self_text(self):
        """点击我进入微信的个人界面 """
        time.sleep(2)
        ele = self.driver.element_by_name('我').text
        return ele



    @teststeps
    def click_contacts(self):
        """点击通讯录进入通讯录列表"""
        time.sleep(2)
        self.driver.element_by_name("通讯录").click()

    @teststeps
    def click_public(self):
        """点击公众号进入公众号列表"""
        time.sleep(2)
        self.driver.element_by_name("公众号").click()

    @teststeps
    def click_start(self):
        """点击万星在线进入万兴公众号"""
        time.sleep(2)
        self.driver.element_by_name("万星在线").click()
    @teststeps
    def account_management(self):
        """点击账户管理"""
        time.sleep(2)
        self.driver.element_by_name("账户管理").click()


    @teststeps
    def click_my_school(self):
        """点击我的学校"""
        time.sleep(2)
        self.driver.element_by_name("我的学校").click()
        print("进入我的学校")

    @teststeps
    def click_school_List(self):
        time.sleep(2)
        self.driver.element_by_name('小玉2额hi湖南省/张家界市/慈利县').click()

    @teststeps
    def show_my_school(self):
        time.sleep(10)
        print("这个学校的名字是：小玉2额hi")










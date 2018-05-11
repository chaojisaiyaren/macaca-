import unittest
import os
from app.weixin.element.main_page import HomePage
from app.weixin.element.master_page import Charge_statistics,MasterPage
import time

from conf.decorator import testcase, setup, teardown
from app.student.login.object_page.login_page import LoginPage



class Charge_statistic(unittest.TestCase):
    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login_page = LoginPage()
        cls.charge_page = Charge_statistics()
        cls.master_page = MasterPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_charge(self):
        self.login_page.weixin_app_status()  # 判断APP当前状态
        self.home.click_contacts()  # 进入通讯录
        self.home.click_public()  # 进入公众号
        self.home.click_start()  # 进入万星在线
        print("进入万星在线成功")
        self.home.account_management()# 点击进入账户管理
        self.home.click_my_school() # 点击进入我的学校
        self.home.show_my_school() # 显示我们的学校
        self.home.click_school_List()# 点击进入学校的列表
        self.charge_page.click_charge()# 点击进入收费统计
        # self.charge_page.click_month()# 点击简报选择某个月份
        # self.charge_page.clcik_determine()# 点击确定
        self.master_page.share_ma()  # 点击右上角的分享按钮
        self.master_page.share_circle_of_friends()  # 点击分享朋友圈
        self.master_page.click_publish()  # 点击发表
        print("分享朋友圈成功！")
        self.master_page.go_back()  # 点击返回回到公众号主页面
        self.master_page.get_btn()  # 点击返回
        self.master_page.go_back()  # 点击返回

        print("demo 测试完毕")


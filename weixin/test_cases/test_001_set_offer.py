#!/usr/bin/env python
# code:UTF-8
# @Author  : Sasuke
import unittest
import os
from app.weixin.element.main_page import HomePage
from app.weixin.element.master_page import MasterPage
import time

from conf.decorator import testcase, setup, teardown
from app.student.login.object_page.login_page import LoginPage
PATH = lambda p: os.path.abspath(os.path.join(os.path.dirname(__file__), p))  # 获取当前路径


class Set_offer(unittest.TestCase):
    """设置优惠价"""

    @classmethod
    @setup
    def setUp(cls):
        """启动应用"""
        cls.home = HomePage()
        cls.login_page = LoginPage()
        cls.master_page = MasterPage()

    @classmethod
    @teardown
    def tearDown(cls):
        pass

    @testcase
    def test_offer(self):
        self.login_page.weixin_app()  # 判断APP当前状态
        self.home.click_contacts()  # 进入通讯录
        self.home.click_public()  # 进入公众号
        self.home.click_start()  # 进入万星在线
        print("进入万星在线成功")
        self.home.account_management()# 点击进入账户管理
        self.home.click_my_school() # 点击进入我的学校
        self.home.show_my_school()  # 显示我们学校的姓名
        self.home.click_school_List()# 点击进入学校的列表

        self.master_page.set_price() # 设置优惠价进入设置优惠条目
        # self.master_page.click_set() # 点击设置按钮
        # self.master_page.set_password() # 点击请输入密码，输入密码为123123

        # self.master_page.click_determine()# 点击确定。
        # self.master_page.enter_price() # 设置价格为150
        # self.master_page.click_determine()  # 点击确定。
        self.master_page.share_offer()# 分享优惠页
        self.master_page.click_now_buy()# 点击现在购买，这个是为了使页面处于一个可以点击的状态
        self.master_page.click_now_buy()  # 这个是选择我们要购买的优惠的卡包
        self.master_page.show_price() # 显示我们的优惠的价格
        self.master_page.click_immediately_buy() # 点击立即购买
        self.master_page.original_price() #显示原来的价格
        self.master_page.now_price() # 显示现在的价格
        self.master_page.student_account() # 换一个学生账号
        self.master_page.student_password()# 填写密码

        self.master_page.click_determine() # 点击确定

        self.master_page.click_pay() # 点击立即支付
        self.master_page.share_ma() #点击右上角的分享按钮
        self.master_page.share_circle_of_friends() #点击分享朋友圈
        self.master_page.click_publish() # 点击发表
        self.master_page.go_back()# 点击返回回到公众号主页面
        self.master_page.get_btn()# 点击返回
        self.master_page.go_back()  # 点击返回

        print("demo 测试完毕")



        time.sleep(1)


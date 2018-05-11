import time
from macaca import WebDriverException
from conf.decorator import teststep, teststeps
from conf.basepage import BasePage


class MasterPage(BasePage):

    @teststeps
    def set_price(self):
        # 点击设置优惠价
        time.sleep(2)
        self.driver.element_by_name("设置优惠价").click()
        ele = self.driver.element_by_name("设置优惠价").text
        print("点击%s"%ele)
        return ele

    @teststeps
    def click_set(self):
        # 点击设置按钮
        time.sleep(2)
        self.driver.element_by_xpath('//android.webkit.WebView[1]/android.view.View[3]/android.view.View[2]/android.view.View[1]').click()

    @teststeps
    def set_password(self):
        # 点击设置按钮
        time.sleep(2)
        self.driver.element_by_xpath('//*[@text="请输入密码"]').send_keys("123123")
        print("成功取到元素！")

    @teststeps
    def click_determine(self):
        # 点击确定按钮
        time.sleep(2)
        self.driver.element_by_xpath('//android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]').click()

    @teststeps
    def enter_price(self):
        # 点击请输入价格
        time.sleep(2)
        self.driver.element_by_name("请输入价格").send_keys("150")

    @teststeps
    def share_offer(self):
        # 分享优惠页
        time.sleep(5)
        self.driver.element_by_xpath("//android.webkit.WebView[1]/android.view.View[8]").click()
        print("点击分享优惠页")

    @teststeps
    def click_now_buy(self):
        # 点击现在购买(目的是让这个页面变成可以点击的)
        time.sleep(2)
        self.driver.element_by_name("现在购买").click()

    def click_immediately_buy(self):
        # 点击立即购买
        time.sleep(5)
        self.driver.element_by_name("立即购买").click()

    @teststeps
    def go_back(self):
        # 点击返回回到公主号主页面
        time.sleep(2)
        self.driver.element_by_id('com.tencent.mm:id/i2').click()

    @teststeps
    def get_btn(self):
        # 点击返回
        time.sleep(2)
        self.driver.element_by_xpath('//*[@resource-id="com.tencent.mm:id/hm"]').click()

    @teststeps
    def share_ma(self):
        # 点击右上角的分享按钮，分享我们的公众号。
        time.sleep(2)
        self.driver.element_by_xpath('//*[@resource-id="com.tencent.mm:id/h1"]/android.support.v7.widget.LinearLayoutCompat[1]').click()

    @teststeps
    def share_circle_of_friends(self):
        # 点击分享朋友圈
        time.sleep(2)
        self.driver.element_by_xpath('//*[@resource-id="com.tencent.mm:id/c9b"]/android.widget.LinearLayout[2]/android.widget.ImageView[1]').click()

    @teststeps
    def click_publish(self):
        # 点击发表
        time.sleep(2)
        self.driver.element_by_name("发表").click()
        print("朋友圈发表公众号成功")

    @teststeps
    def click_drop_down(self):
        pass

    @teststeps
    def student_account(self):
        # 重新输入支付的学生账号
        time.sleep(2)
        self.driver.element_by_xpath('//*[@text="13812341234"]').send_keys("19999999999")

    @teststeps
    def student_password(self):
        # 重新输入学生的密码
        time.sleep(2)
        self.driver.element_by_xpath('//*[@text="••••••"]').send_keys("123321")

    @teststeps
    def click_pay(self):
        # 点击立即支付
        time.sleep(2)
        self.driver.element_by_xpath('//android.webkit.WebView[1]/android.view.View[1]/android.view.View[9]/android.view.View[2]').click()

    #优惠价￥ 150
    def show_price(self):
        #显示优惠价格
        print("优惠价格是：150元")


    # 显示我们的原价和现在的价格
    def now_price(self):
        print("优惠之后的价格是：150元")
    def original_price(self):
        print("优惠前的价格是：183元")

    def click_buy_protocol(self):
        # 点击购买协议
        pass

class Charge_statistics(BasePage):
    """这个是收费统计"""

    @teststeps
    def click_charge(self):
        # 点击收费统计
        time.sleep(2)
        self.driver.element_by_xpath('//android.webkit.WebView[1]/android.view.View[3]/android.view.View[5]/android.view.View[2]').click()
    @teststeps
    def click_month(self):
        time.sleep(2)
        self.driver.element_by_xpath('//android.webkit.WebView[1]/android.view.View[3]/android.view.View[2]/android.view.View[1]').click()

    def clcik_determine(self):
        time.sleep(2)
        self.driver.element_by_name("确定").click()




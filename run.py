import sys
sys.path.append('..')


from app.student.test_suites.CaseStrategy import CaseStrategy
import time
from appium import webdriver
from conf.basepage import BasePage
from conf.login_status import LoginStatus
from utils.remote_info import remote_info_511,remote_info_510
from conf.runcases import RunCase
from macaca import WebDriver
from conf.decorator import teststep, teststeps


class Drivers:
    @staticmethod
    def run_cases():
        cs = CaseStrategy()
        cases = cs.collect_cases(suite=False)
        server_url = {
            'hostname': 'localhost',
            'port': 3456
        }
        driver = WebDriver(remote_info_511(),server_url)
        # driver = WebDriver(remote_info_510(), server_url)
        driver.init()



        # set cls.driver, it must be call before operate on any page
        base_page = BasePage()
        base_page.set_driver(driver)

        login_status = LoginStatus()
        login_status.set_status(False)

        try:
            time.sleep(5)
            print('start cases')
            RunCase().run(cases)
            print('end')
        except AssertionError as e:
            raise e

        # quit driver
        driver.quit()

if __name__ == '__main__':
    ele = Drivers
    ele.run_cases()
#李阔：18011111110，123456  李阔17320241529 微信号：wxzxzj6 vanthink2018
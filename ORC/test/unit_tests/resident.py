import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class resident(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_resident(self):
        user = "Resident"
        pwd = "maverick1a"
        driver = self.driver
        driver.maximize_window()
        driver.get("https://team3-orc-project.herokuapp.com/accounts/login/")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("https://team3-orc-project.herokuapp.com/home/")
        assert "Logged In"
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='wrapper']/ul/li/a/span").click()
        time.sleep(1)
        driver.get("https://team3-orc-project.herokuapp.com/workorder/new/")
        time.sleep(1)
        select = Select(driver.find_element_by_xpath("//*[@id='id_resident_name']"))
        select.select_by_index(1)
        time.sleep(1)
        elem=driver.find_element_by_id("id_workorder_id")
        elem.send_keys("13")
        select = Select(driver.find_element_by_xpath("//*[@id='id_resident_id']"))
        select.select_by_index(1)
        elem = driver.find_element_by_id("id_workorder_Description")
        elem.send_keys("Gas stove")
        select = Select(driver.find_element_by_xpath("//*[@id='id_workorder_category']"))
        select.select_by_index(1)
        select = Select(driver.find_element_by_xpath("//*[@id='id_workorder_priority']"))
        select.select_by_index(1)
        select = Select(driver.find_element_by_xpath("// *[ @ id = 'id_property_number']"))
        select.select_by_index(1)
        elem = driver.find_element_by_id("id_workorder_opendate")
        elem.send_keys()
        elem = driver.find_element_by_id("id_workorder_duedate")
        elem.send_keys()
        elem = driver.find_element_by_id("id_workorder_closedate")
        elem.send_keys()
        time.sleep(1)
        driver.find_element_by_xpath("//*[@id='content']/form/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='navbarResponsive']/ul/li[2]").click()
        time.sleep(2)
        driver.get("https://team3-orc-project.herokuapp.com/about/")
        time.sleep(1)

        def tearDown(self):
            self.driver.close()
            time.sleep(10)

    if __name__ == "__main__":
        unittest.main()
import unittest
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class maintenanceworker(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_maintenanceworker(self):
        user = "Maintenanceworker"
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
        driver.get("https://team3-orc-project.herokuapp.com/maintenancework/3/workerview/")
        driver.get("https://team3-orc-project.herokuapp.com/maintenancework/new/")
        select = Select(driver.find_element_by_xpath("//*[@id='id_residentid']"))
        select.select_by_index(1)
        time.sleep(1)
        driver.find_element_by_id("id_maintenancework_description").send_keys("loose tap")
        select = Select(driver.find_element_by_id("id_workorder_id"))
        select.select_by_index(1)
        select = Select(driver.find_element_by_id("id_maintenanceworker_name"))
        select.select_by_index(1)
        select = Select(driver.find_element_by_id("id_property_number"))
        select.select_by_index(1)
        select = Select(driver.find_element_by_id("id_equipment_name"))
        select.select_by_index(1)
        driver.find_element_by_id("id_maintenancework_cost").send_keys("23")
        driver.find_element_by_id("id_maintenancework_opendate").send_keys()
        driver.find_element_by_id("id_maintenancework_duedate").send_keys()
        driver.find_element_by_id("id_maintenancework_closedate").send_keys()
        driver.find_element_by_xpath("//*[@id='content']/form/button").click()
        time.sleep(3)
        driver.get("https://team3-orc-project.herokuapp.com/equipment_list/")
        time.sleep(2)
        driver.get("https://team3-orc-project.herokuapp.com/about/")
        time.sleep(1)



        def tearDown(self):
            self.driver.close()
            time.sleep(10)

    if __name__ == "__main__":
        unittest.main()
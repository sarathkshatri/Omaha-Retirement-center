import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class TestORCMaintenanceWork(unittest.TestCase):

    def setUp(self) :
        self.driver = webdriver.Chrome()

    def test_orc(self):
        user = "instructor"
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

        time.sleep(1)
        #Click on Maintenace Work Tab
        elem = driver.find_element_by_xpath(" //*[@id=\"wrapper\"]/ul/li[2]/a")
        elem.click()
        time.sleep(1)

        # Clicks on new maintenance work button
        elem = driver.find_element_by_xpath("/html/body/div[1]/ul/a").click()
        time.sleep(1)

        # fill the maintenance work details
        elem = driver.find_element_by_id("id_residentid")
        elem.send_keys("Resident")
        elem = driver.find_element_by_id("id_maintenancework_description")
        elem.send_keys("Gas stove is not working")
        elem = driver.find_element_by_id("id_workorder_id")
        elem.send_keys("2")
        elem = driver.find_element_by_id("id_maintenanceworker_name")
        elem.send_keys("Joel Franklin")
        elem = driver.find_element_by_id("id_property_number")
        elem.send_keys("Atlas101")
        elem = driver.find_element_by_id("id_equipment_name")
        elem.send_keys("toolbox")
        elem = driver.find_element_by_id("id_maintenancework_cost")
        elem.send_keys("100")
        time.sleep(1)

        # xpath, clicks on save button for maintenance work
        elem = driver.find_element_by_xpath("/html/body/div[1]/form/button").click()
        time.sleep(1)

        # xpath, clicks on edit
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/strong[9]/a").click()
        time.sleep(1)

        # Edit maintenance work details
        elem = driver.find_element_by_id("id_maintenancework_cost")
        elem.clear()
        elem.send_keys("20")
        time.sleep(1)

        # xpath, clicks on update button for maintenance work

        elem = driver.find_element_by_xpath("/html/body/div[1]/form/button").click()
        time.sleep(1)

        # xpath, clicks on delete maintenance work button

        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/div/div/strong[10]/a").click()
        time.sleep(1)

        driver.switch_to.alert.accept()
        time.sleep(1)

        # Click on Maintenace Worker Tab

        elem = driver.find_element_by_xpath(" //*[@id=\"wrapper\"]/ul/li[4]/a")
        elem.click()
        time.sleep(1)

        # Clicks on new maintenance worker button

        elem = driver.find_element_by_xpath("/html/body/div[1]/a").click()
        time.sleep(1)

        # fill the maintenance worker  details
        elem = driver.find_element_by_id("id_user")
        elem.send_keys("RamuKaka")
        elem = driver.find_element_by_id("id_maintenanceworker_name")
        elem.send_keys("Robert")
        elem = driver.find_element_by_id("id_worker_emailaddress")
        elem.send_keys("rg@yahoo.com")
        elem = driver.find_element_by_id("id_worker_address")
        elem.send_keys("5555")
        elem = driver.find_element_by_id("id_worker_yearsofexperience")
        elem.send_keys("25")
        elem = driver.find_element_by_id("id_worker_contactdetails")
        elem.send_keys("2222")

        time.sleep(1)

        # xpath, clicks on save button for maintenance worker

        elem = driver.find_element_by_xpath("/html/body/div[1]/form/button").click()
        time.sleep(1)

        # xpath, clicks on edit

        elem = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td[10]/a").click()
        time.sleep(2)

        # Edit maintenance worker details
        elem = driver.find_element_by_id("id_worker_yearsofexperience")
        elem.clear()
        elem.send_keys("30")
        time.sleep(1)

        # xpath, clicks on update button for maintenance worker
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/form/button").click()
        time.sleep(1)

        # xpath, clicks on delete maintenance worker button

        elem = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td[11]/a").click()
        time.sleep(1)

        driver.switch_to.alert.accept()
        time.sleep(1)


        elem = driver.find_element_by_xpath('//*[@id="wrapper"]/ul/li[6]/a')
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath('//*[@id="content"]/a')
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("//*[@id='id_user']")
        elem.send_keys("RamuKaka")
        elem = driver.find_element_by_xpath('//*[@id="id_orc_staff_name"]')
        elem.send_keys("sarath")
        elem = driver.find_element_by_xpath('//*[@id="id_orc_staff_emailaddress"]')
        elem.send_keys("skshatri@gmail.com")
        elem = driver.find_element_by_xpath('//*[@id="id_orc_staff_address"]')
        elem.send_keys("Street:Q")
        elem = driver.find_element_by_xpath('//*[@id="id_orc_staff_yearsofexperience"]')
        elem.send_keys("4")
        elem = driver.find_element_by_xpath('//*[@id="id_orc_staff_contactdetails"]')
        elem.send_keys("999999999")
        elem = driver.find_element_by_xpath('//*[@id="id_orc_staff_position"]')
        elem.send_keys("staff")
        elem = driver.find_element_by_xpath('//*[@id="content"]/form/button')
        elem.click()
        time.sleep(1)
        elem = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td[12]/a").click()
        time.sleep(1)

        driver.switch_to.alert.accept()
        time.sleep(1)

        driver.get("http://team3-orc-project.herokuapp.com/resident_list/")
        driver.get("http://team3-orc-project.herokuapp.com/resident/new/")
        elem = driver.find_element_by_xpath('//*[@id="id_user"]')
        elem.send_keys("RamuKaka")
        elem = driver.find_element_by_xpath('//*[@id="id_resident_name"]')
        elem.send_keys("SK")
        elem = driver.find_element_by_xpath('//*[@id="id_resident_occupation"]')
        elem.send_keys("FBI")
        elem = driver.find_element_by_xpath('//*[@id="id_resident_emailaddress"]')
        elem.send_keys("sk@gmail.com")
        elem = driver.find_element_by_xpath('//*[@id="id_resident_marital_status"]')
        elem.send_keys("Single")
        elem = driver.find_element_by_xpath('//*[@id="id_resident_familymember_count"]')
        elem.send_keys('2')
        elem = driver.find_element_by_xpath('//*[@id="id_resident_petdetails"]')
        elem.send_keys('1')
        elem = driver.find_element_by_xpath('//*[@id="id_resident_contactdetails"]')
        elem.send_keys('9999999999')
        elem = driver.find_element_by_xpath('//*[@id="content"]/form/button')
        elem.click()
        driver.get("http://team3-orc-project.herokuapp.com/resident_list/")
        time.sleep(2)
        elem = driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td[13]/a").click()
        time.sleep(1)

        driver.switch_to.alert.accept()
        time.sleep(1)





def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()



def tearDown(self):
    self.driver.close()

if __name__ == "__main__":
    unittest.main()
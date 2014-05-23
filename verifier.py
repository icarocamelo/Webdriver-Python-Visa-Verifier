from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Visa(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.vfsglobal.ca"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_visa(self):
        driver = self.driver
        driver.get(self.base_url + "/Canada/Brazil/track_your_application.html")
	time.sleep(5)
        trackingId = driver.find_element_by_id("ctl00_CPH_txtTrackingId")

	if (trackingId == null):
		self.driver.quit()
	else:
		print trackingId

        driver.find_element_by_id("ctl00_CPH_txtTrackingId").send_keys("20140000BRSAWKR00000") #trackingId
        driver.find_element_by_id("ctl00_CPH_txtDOB_txtDate").clear()
        driver.find_element_by_id("ctl00_CPH_txtDOB_txtDate").send_keys("01/01/1900") #birthday
        driver.find_element_by_id("ctl00_CPH_btnDOB").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

logging.basicConfig(filename="log.txt", level=logging.INFO)


class TestExamples(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Remote(
            command_executor="http://192.168.110.167:4444/wd/hub",
            desired_capabilities=DesiredCapabilities.FIREFOX)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()  # Note: driver.maximize_window does not work on Linux, instead set window size and window position like driver.set_window_position(0,0) and driver.set_window_size(1920,1080)

    def test_one(self):
        try:
            driver = self.driver
            driver.get("http://www.python.org")
            self.assertIn("Python", driver.title)
            elem = driver.find_element_by_name("q")
            elem.send_keys("documentation")
            elem.send_keys(Keys.RETURN)
            assert "No results found." not in driver.page_source
        finally:
            logging.info("Test One Video: "  + driver.session_id)

    def test_two(self):
        try:
            driver = self.driver
            driver.get("http://www.google.com")
            elem = driver.find_element_by_name("q")
            elem.send_keys("webdriver")
            elem.send_keys(Keys.RETURN)
        finally:
            logging.info("Test Two Video: "  + driver.session_id)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# import logging



# @pytest.yield_fixture(scope="session")
# def mydriver(request):
#     logging.debug("In mydriver fixture")
#     nodeUrl = "http://192.168.111.250:4444/wd/hub"
#     selenium = webdriver.Remote(command_executor=nodeUrl, desired_capabilities=DesiredCapabilities.CHROME)
#     selenium.get('http://192.168.192.251/mrx/')
#     yield selenium
#     selenium.quit()


import logging
import pytest
@pytest.fixture
def selenium(selenium):
    logging.debug("In Overridden Selenium fixture")
    selenium.set_window_size(1280,1024)
    return selenium



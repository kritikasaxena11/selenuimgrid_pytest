
import pytest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from datetime import datetime





import urllib2
import pytest


# #@pytest.mark.nondestructive
# def test_example2(base_url):
#     logging.debug("urllib2.urlopen(base_url).getcode(): " +str(urllib2.urlopen(base_url).getcode()))
#     assert 200 == urllib2.urlopen(base_url).getcode()
#     # logging.debug("Base_url: " + base_url )
#     # return base_url





def test_example1(selenium,base_url):
    logging.debug("In test_example1")
    #mydriver.get('http://www.google.com')



def test_example3(selenium,base_url):
    logging.debug("In test_example3")
    #mydriver.get('http://www.facebook.com')



def test_example5(selenium,base_url):
    logging.debug("In test_example5")

    #mydriver.get('https://www.jetbrains.com/')



def test_example4(selenium,base_url):
    logging.debug("In test_example4")
    #selenium.get('http://192.168.192.251/mrx/')

    logging.info("Hitting Base Url:  " + base_url)
    selenium.get(base_url)
    logging.info("Base Url Hit:  " + base_url)


    try:
        logging.info("Username Start time: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        elem_username = WebDriverWait(selenium, 30).until(EC.presence_of_element_located((By.ID, "username")))

        logging.debug("Element:  " + str(elem_username))
    except Exception as e:
        logging.info("Exception occurred while waiting for input username textbox: " +str(e) )



    try:
        logging.info("Password  Start time: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        elem_password = WebDriverWait(selenium, 30).until(EC.presence_of_element_located((By.ID, "password")))

    except Exception as e:
        logging.info("Exception occurred while waiting for input password textbox: " + str(e))



    logging.info("End time: " + datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    elem_username.clear()
    elem_username.send_keys("admin")
    elem_password.clear()
    elem_password.send_keys("abc125")
    elem_password.send_keys(Keys.RETURN)
    time.sleep(15)
    #assert False





# def test_example4(selenium):
#     selenium.get('http://192.168.192.251/mrx/')
#     #selenium.find_element_by_id('username').send_keys('chakry.gkkkk')
#     #elem = selenium.find_elements_by_class_name("form-control ng-untouched ng-pristine ng-invalid")
#     time.sleep(15)
#     elem = selenium.find_element_by_id('username')
#     #elem = selenium.find_element_by_xpath('//*[@id="username"]')
#     elem.clear()
#     elem.send_keys("admin")
#     elem = selenium.find_element_by_id('password')
#     #elem = selenium.find_element_by_xpath('//*[@id="password"]')
#     elem.clear()
#     elem.send_keys("abc125")
#     elem.send_keys(Keys.RETURN)
#     time.sleep(15)






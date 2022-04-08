import pytest
import sys

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import logging
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# @pytest.fixture()
#@pytest.mark.skip(reason="kritikaaaa")
#@pytest.mark.skipif(sys.version_info < (3,5), reason="kritikaaaa")
@pytest.mark.mac
def test_driver():
    a =67.8
    assert "hey" + str(a) == "hey67.8"





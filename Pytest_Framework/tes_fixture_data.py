import pytest
import self
from selenium import webdriver
from Pytest_Framework.BaseClass import BaseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(BaseClass):

    def test_editprofile(self , dataload):
        log=self.test_loggingDemo()
        log.info(dataload[2])
        print(dataload)


@pytest.fixture(params=["chrome", "firefox"],scope="class")
def browser(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
    elif request.param == "firefox":
        driver = webdriver.Firefox()
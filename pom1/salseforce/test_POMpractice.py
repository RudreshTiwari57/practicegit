import pytest
import xdist
from Base import OpeningBrowser,log_on_failure
import allure
from tre import BaseTest
from login import login
from exceldata import exceldata
import Base
from selenium import webdriver

class Testuses(BaseTest):
    @pytest.mark.parametrize("username,password",exceldata("UserData"))
    def test_salseforce(self,username,password):
        l = login(self.driver)
        print("username -- ",username,"        ","password -- ",password)
        l.usersignin(username,password)
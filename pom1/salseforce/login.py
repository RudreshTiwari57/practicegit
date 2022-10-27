from selenium import webdriver
from selenium.webdriver.common.by import By
from generaldata import data
from setwisesignin import stepwisesignin

class login(stepwisesignin):
    def __init__(self,self1):
        super().__init__(self1)
    def usersignin(self,username,password):
        self.username("Username_xpath",username)
        self.password("Password_xpath", password)
        self.loginbutton("LoginButtonm_xpath")



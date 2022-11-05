import time

from Utilities.configreader import ConfigReader
from features.pageobject.Base import BaseSettingsPage



class Search(BaseSettingsPage):
    def __init__(self,driver):
        super().__init__(driver)
    def OpenPage(self,url):
        self.driver.get(url)
        self.DynamicImplicitWait(40)
    def clickclose(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("close_XPATH")
    def Click_loginhomepage(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINHOMEPAHEBUTTON_XPATH")
    def Enter_Username(self,username):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("USERNAME_XPATH",username)
    def Enter_password(self,password):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("PASSWORD_XPATH", password)
    def Click_login(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOGINBUTTON_XPATH")
    def text_Searchbar(self,searchTEXT):
        self.DynamicImplicitWait(40)
        self.TypeEditBox("SEARCHBAR_XPATH",searchTEXT)
    def Click_SEARCHBUTTON(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("SEARCHBUTTON_XPATH")

    def Check_Relevance(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("RELAVENCE_XPATH")
        time.sleep(5)


    def Check_POPULARITY(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("POPULARITY_XPATH")
        time.sleep(5)


    def Check_LOWTOHIGH(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("LOWTOHIGH_XPATH")
        time.sleep(5)



    def Check_HIGHTOLOW(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("HIGHTOLOW_XPATH")
        time.sleep(5)


    def Check_NEWESTFIRST(self):
        self.DynamicImplicitWait(40)
        self.ClickButton("NEWESTFIRST_XPATH")
        time.sleep(5)






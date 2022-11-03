from selenium import webdriver
from generaldata import data


class stepwisesignin:
    def __init__(self,driver):
        self.driver = driver
    def username(self,locater,name):
        #self.driver = webdriver.Chrome()
        if locater.endswith("_xpath"):
            self.driver.find_element_by_xpath(data("locaters", locater)).click()
            self.driver.find_element_by_xpath(data("locaters", locater)).send_keys(name)

        elif locater.endswith("_id"):
            self.driver.find_element_by_id(data("locaters", locater)).click()
            self.driver.find_element_by_id(data("locaters", locater)).send_keys(name)


        elif locater.endswith("_css_selector"):
            self.driver.find_element_by_css_selector(data("locaters", locater)).click()
            self.driver.find_element_by_css_selector(data("locaters", locater)).send_keys(name)


        elif locater.endswith("_class_name"):
            self.driver.find_element_by_class_name(data("locaters", locater)).click()
            self.driver.find_element_by_class_name(data("locaters", locater)).send_keys(name)


        elif locater.endswith("_tag_name"):
            self.driver.find_element_by_tag_name(data("locaters", locater)).click()
            self.driver.find_elements__tag_name(data("locaters", locater)).send_keys(name)


        else:
            self.driver.find_element_by_name(data("locaters", locater)).click()
            self.driver.find_elements_by_name(data("locaters", locater)).send_keys(name)

    def password(self, locater, name):
        if locater.endswith("_xpath"):
            self.driver.find_element_by_xpath(data("locaters", locater)).click()
            self.driver.find_element_by_xpath(data("locaters", locater)).send_keys(name)

        elif locater.endswith("_id"):
            self.driver.find_element_by_id(data("locaters", locater)).click()
            self.driver.find_element_by_id(data("locaters", locater)).send_keys(name)


        elif locater.endswith("_css_selector"):
            self.driver.find_element_by_css_selector(data("locaters", locater)).click()
            self.driver.find_element_by_css_selector(data("locaters", locater)).send_keys(name)


        elif locater.endswith("_class_name"):
            self.driver.find_element_by_class_name(data("locaters", locater)).click()
            self.driver.find_element_by_class_name(data("locaters", locater)).send_keys(name)


        elif locater.endswith("_tag_name"):
            self.driver.find_element_by_tag_name(data("locaters", locater)).click()
            self.driver.find_elements__tag_name(data("locaters", locater)).send_keys(name)


        else:
            self.driver.find_element_by_name(data("locaters", locater)).click()
            self.driver.find_elements_by_name(data("locaters", locater)).send_keys(name)

    def loginbutton(self, locater):
        if locater.endswith("_xpath"):
            self.driver.find_element_by_xpath(data("locaters", locater)).click()

        elif locater.endswith("_id"):
            self.driver.find_element_by_id(data("locaters", locater)).click()

        elif locater.endswith("_css_selector"):
            self.driver.find_element_by_css_selector(data("locaters", locater)).click()

        elif locater.endswith("_class_name"):
            self.driver.find_element_by_class_name(data("locaters", locater)).click()


        elif locater.endswith("_tag_name"):
            self.driver.find_element_by_tag_name(data("locaters", locater)).click()
        else:
            self.driver.find_element_by_name(data("locaters", locater)).click()

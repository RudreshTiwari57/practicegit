import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given(u'you are on youtube home page')
def step_impl(context):
    context.driver.get('https://www.youtube.com/')
@when(u'Validate home page title')
def step_impl(context):

    actTitle = "YouTube"
    assert actTitle in context.driver.title


@then(u'Enter peaky blinders')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input").send_keys("peaky blinders")


@then(u'hit search button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/button").click()
    time.sleep(5)

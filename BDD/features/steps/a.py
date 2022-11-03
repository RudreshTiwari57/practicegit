import time

from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given(u'I navigate to google.com')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Given I navigate to google.com')
    context.driver.maximize_window()
    context.driver.get("http://google.com")
    context.driver.implicitly_wait(5)



@when(u'I validate the page title')
def step_impl(context):
    # raise NotImplementedError(u'STEP: When I validate the page title')
    title = context.driver.title
    print("Title is " + title)
    assert "Google" in title


@then(u'I enter the text as "{searchText}"')
def step_impl(context, searchText):
    # raise NotImplementedError(u'STEP: Then I enter the text as "Hello Selenium"')
    context.driver.find_element_by_name("q").send_keys(searchText)
    time.sleep(3)


@then(u'I click the search button')
def step_impl(context):
    # raise NotImplementedError(u'STEP: Then I click the search button')
    context.driver.find_element_by_name("btnK").submit()
    time.sleep(3)


from behave import *
from Utilities.configreader import ConfigReader
from features.pageobject.search import Search



@given(u'We are on flipkart website')
def step_impl(context):
    context.search = Search(context.driver)
    context.search.OpenPage(ConfigReader("base info","URL"))
    context.search.clickclose()



@when(u'click login')
def step_impl(context):
    context.search.Click_loginhomepage()


@then(u'Enter your "{username}" in the feild')
def step_impl(context,username):
    context.search.Enter_Username(username)


@then(u'Enter your "{password}" in the box')
def step_impl(context,password):
    context.search.Enter_password(password)


@then(u'click login')
def step_impl(context):
    context.search.Click_login()


@then(u'type "{searchTEXT}" in search bar')
def step_impl(context,searchTEXT):
    context.search.text_Searchbar(searchTEXT)


@then(u'Click on search button')
def step_impl(context):
    context.search.Click_SEARCHBUTTON()


@then(u'Check on Relevance is clickable')
def step_impl(context):
    context.search.Check_Relevance()


@then(u'Check on popularity is clickable')
def step_impl(context):
    context.search.Check_POPULARITY()


@then(u'Check on Price low-high is clickable')
def step_impl(context):
    context.search.Check_LOWTOHIGH()


@then(u'Check on Price high-low is clickable')
def step_impl(context):
    context.search.Check_HIGHTOLOW()


@then(u'Check on newest first is clickable')
def step_impl(context):
    context.search.Check_NEWESTFIRST()



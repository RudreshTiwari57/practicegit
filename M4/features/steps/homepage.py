import time

from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select



@given(u'you are on home page')
def step_impl(context):
    context.driver.get("https://courses.letskodeit.com/practice")


@when(u'validate title')
def step_impl(context):
    actualtitle = "Practice Page"
    assert actualtitle in context.driver.title


@then(u'click on benz radio button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[1]/div[1]/fieldset/label[2]/input").click()


@then(u'select honda from dropdown')
def step_impl(context):
    DD = Select(context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/fieldset/select"))
    DD.select_by_value("honda")
    time.sleep(10)


@then(u'select apple and peace from list')
def step_impl(context):

    dd1 = Select(context.driver.find_element(By.XPATH, "//*[@id='multiple-select-example']"))
    allopt = dd1.options
    for opt in allopt:
        if opt.text == "Apple":
            opt.click()
        if opt.text == "Peach":
            opt.click()
    time.sleep(3)


@then(u'deselect apple')
def step_impl(context):
    dd1 = Select(context.driver.find_element(By.XPATH, "//*[@id='multiple-select-example']"))
    dd1.deselect_by_value("apple")


@then(u'select honda checkbox')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[1]/div[4]/fieldset/label[3]/input").click()



@then(u'click on open window')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[1]/fieldset/button").click()



@then(u'switch to new window')
def step_impl(context):
    global driverbf
    driverbf = context.driver.window_handles[0]
    driveraft = context.driver.window_handles[1]
    context.driver.switch_to.window(driveraft)


@then(u'get the text all courses')
def step_impl(context):
    #context.driver = webdriver.Chrome(ChromeDriverManager().install())
    print("you have to look here",context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div/div[1]/h1").text)
    time.sleep(5)
    context.driver.close()



@then(u'click on open tab')
def step_impl(context):
    context.driver.switch_to.window(driverbf)
    context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[2]/fieldset/a").click()

@then(u'switch to new tab')
def step_impl(context):
    #context.driver = webdriver.Chrome(ChromeDriverManager().install())
    driveraft = context.driver.window_handles[1]
    context.driver.switch_to.window(driveraft)


@then(u'get text category text')
def step_impl(context):
    print("you have to look here 2 ",context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div/div[2]/div[1]/label").text)



@then(u'Fill your name')
def step_impl(context):
    context.driver.switch_to.window(driverbf)
    context.driver.find_element(By.XPATH, "//*[@id='name']").send_keys("Rudresh")


@then(u'click on alert button')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//*[@id='alertbtn']").click()


@then(u'get text for alert window and click on the ok button')
def step_impl(context):
    t3 = context.driver.switch_to_alert()
    print(t3.text)
    t3.accept()





@then(u'enter your name')
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[2]/div[3]/fieldset/input[1]").send_keys("Rudresh")


@then(u'click on conform button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='confirmbtn']").click()
    time.sleep(3)

@then(u'get text for alert window and click on cancel button')
def step_impl(context):
    t4 = context.driver.switch_to_alert()
    print(t4.text)
    t4.dismiss()


@then(u'get the data for first row and first column')
def step_impl(context):
    context.driver.switch_to.window(driverbf)
    a = context.driver.find_elements(By.TAG_NAME, "tr")
    print()
    print(a[0].text)
    a = context.driver.find_elements(By.CLASS_NAME, "author-name")

    print()
    for i in a:
        print(i.text)


@then(u'hover on mouse hover')
def step_impl(context):
    context.driver.switch_to.window(driverbf)
    context.driver.execute_script("window.scrollTo(200, 200)")
    AA = ActionChains(context.driver)
    AA.move_to_element(context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/fieldset/div/button"))
    AA.perform()


@then(u'click on top')
def step_impl(context):
    AA = ActionChains(context.driver)
    AA.move_to_element(context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/fieldset/div/div/a[1]"))
    AA.click(context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[4]/div/fieldset/div/div/a[1]"))
    AA.perform()
    time.sleep(5)


@then(u'get the text practice page')
def step_impl(context):
    print(context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/div/h1").text)


@then(u'click on javascript for bigineers')
def step_impl(context):
    context.driver.switch_to.frame(context.driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/div/div[5]/fieldset/iframe"))

    context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div/div/div/div/div/div[3]/div[1]/div/a").click()


@then(u'click on enroll now')
def step_impl(context):
    context.driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/button").click()

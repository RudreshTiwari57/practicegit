import allure
import pytest
from allure_commons.types import AttachmentType
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
import configparser
from selenium.webdriver.chrome.options import Options
import time



@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep



@pytest.fixture()
def log_on_failure(request, OpeningBrowser):
    yield
    item = request.node
    driver = OpeningBrowser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Failure", attachment_type=AttachmentType.PNG)


@pytest.fixture(params=["chrome"], scope="function")
def OpeningBrowser(request):
    # option = Options()
    # option.headless = True
    config = configparser.ConfigParser()
    config.read("C:\pom1\salseforce\config.ini")
    if request.param == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif request.param == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
    else:
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())



    request.cls.driver = driver
    driver.maximize_window()
    driver.get(config["test url"]["url"])
    driver.implicitly_wait(10)


    yield driver
    time.sleep(2)
    driver.quit()
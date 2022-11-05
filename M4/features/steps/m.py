from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.in/")
a = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[1]/div[1]/a").text
print(a)
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./chromedriver")
url = 'https://google.com'
driver.get(url)

driver.find_element(By.CSS_SELECTOR, ".gLFyf.gsfi").send_keys("파이썬")
driver.find_element(By.CSS_SELECTOR, ".gLFyf.gsfi").send_keys(Keys.ENTER)
driver.find_element(By.CSS_SELECTOR, ".LC20lb.MBeuO.DKV0Md").click()
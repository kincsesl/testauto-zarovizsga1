import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("https://barathegyi.web25.hu/")

gomb = driver.find_element_by_id("selectContainer").find_element_by_class_name("link-button")
if gomb.text == "magyar":
    gomb.click()


log = True
while log:
        #time.sleep(2)
        kurrens = driver.find_element_by_xpath("//li[@class = 'current']")
        print(kurrens.text)
        kovetkezo = driver.find_element_by_xpath("//div[@class = 'link-button next']/a")
        kovetkezo.click()
        #time.sleep(1)
driver.close()
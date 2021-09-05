import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://witty-hill-0acfceb03.azurestaticapps.net/stopwatch.html"
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get(url)
ora = driver.find_element_by_class_name("stopwatch")
startgomb = driver.find_element_by_id("start")
stopgomb = driver.find_element_by_id("stop")
restartgomb = driver.find_element_by_id("restart")
lista = []


def listtostring(l):
    s = ""
    for elem in l:
        s += elem
    return s


def test_01():
    assert ora.text == "00: 00: 00"


def test_02():
    global lista
    driver.refresh()
    startgomb = driver.find_element_by_id("start")
    stopgomb = driver.find_element_by_id("stop")
    ora = driver.find_element_by_class_name("stopwatch")
    startgomb.click()
    time.sleep(6)
    stopgomb.click()
    lista = ora.text.split(": ")
    assert lista[0] == "00" and lista[1] == "06"


def test_03():
    global lista
    driver.refresh()
    startgomb = driver.find_element_by_id("start")
    stopgomb = driver.find_element_by_id("stop")
    ora = driver.find_element_by_class_name("stopwatch")
    startgomb.click()
    stopgomb.click()
    ujlista = ora.text.split(": ")
    assert listtostring(ujlista) < listtostring(lista)
    driver.close()



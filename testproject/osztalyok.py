from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import lokatorok
import time

"""
from selenium.webdriver.support.ui import Select
def select(name, index):
    Select(driver.find_element_by_name(name)).select_by_index(index)  
select("bf_time", 1)
select("bf_hours", 1)
"""


class Test_feladat01():
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url01)

    def test_tesztel(self, a, b, c): #Az a és b bemenőkkel c-t kell kapnia.
        self.amezo = self.driver.find_element_by_xpath(lokatorok.a01)
        self.amezo.clear()
        self.amezo.send_keys(a)
        self.bmezo = self.driver.find_element_by_xpath(lokatorok.b01)
        self.bmezo.clear()
        self.bmezo.send_keys(b)
        self.driver.find_element_by_id("submit").click()  # Submit
        time.sleep(1)
        self.cmezo = self.driver.find_element_by_xpath(lokatorok.result01)
        return self.cmezo.text == c


class Test_feladat02():
    def __init__(self):
        self.options = Options()
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url02)


class Test_feladat03():
    def __init__(self):
        self.options = Options()
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url03)


class Test_feladat04():
    def __init__(self):
        self.options = Options()
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url04)


class Test_feladat05():
    def __init__(self):
        self.options = Options()
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url05)

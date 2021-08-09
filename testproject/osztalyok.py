from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import randomstring
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
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url01)

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



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


class Test_feladat01():  # Kerület.
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url01)

    def test_tesztel(self, a, b, c):  # Az a és b bemenőkkel c-t kell kapnia.
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


class Test_feladat02():  # Fejek.
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url02)

    def test_tesztel(self):  # Hadd menjen!
        for i in range(99):  # 100 kattintás.
            self.driver.find_element_by_id(lokatorok.submit02).click()
        self.lista = self.driver.find_element_by_id(lokatorok.ul02).find_elements_by_xpath("//li")
        self.hanyfej = 0
        for elem in self.lista:
            if elem.text == "fej":  # Ha fej, +1-
                self.hanyfej += 1
        return self.hanyfej >= 30


class Test_feladat03():  # Számolgat.
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url03)

    def test_tesztel(self):
        def osszead(a, b):
            return a + b

        def kivon(a, b):
            return a - b

        def szoroz(a, b):
            return a * b

        def oszt(a, b):  # Úgyse lesz ilyen! :)
            return a / b

        self.elso = float(self.driver.find_element_by_id(lokatorok.op1).text)
        self.masodik = float(self.driver.find_element_by_id(lokatorok.op2).text)
        self.muvelet = self.driver.find_element_by_id(lokatorok.muvelet).text
        if self.muvelet == "+":  # A művelettől függően.
            self.eredmeny = osszead(self.elso, self.masodik)
        elif self.muvelet == "-":
            self.eredmeny = kivon(self.elso, self.masodik)
        elif self.muvelet == "*":
            self.eredmeny = szoroz(self.elso, self.masodik)
        else:
            self.eredmeny = oszt(self.elso, self.masodik)
        # print(self.eredmeny, self.elso, self.muvelet, self.masodik)
        self.driver.find_element_by_id(lokatorok.submit03).click()
        return str(int(self.driver.find_element_by_id(lokatorok.eredmeny03).text)) == str(int(self.eredmeny))


class Test_feladat04():
    def __init__(self):
        self.options = Options()
        # options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url04)


class Test_feladat05():
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url05)

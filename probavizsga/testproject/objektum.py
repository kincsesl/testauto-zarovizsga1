import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import lokatorok


class Test_feladat01():  # Terület.
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url)

    def tesztel(self, be, ki):
        self.inputmezo = self.driver.find_element_by_id(lokatorok.input_id)
        self.inputmezo.clear()
        self.inputmezo.send_keys(be)
        self.driver.find_element_by_id(lokatorok.button_id).click()
        return self.driver.find_element_by_id(lokatorok.result_id).text == ki


class Test_feladat02():  # Kártya.
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url2)

    def tesztel(self):
        self.gomb = self.driver.find_element_by_id(lokatorok.button_id)
        for i in range(52):
            self.gomb.click()
        self.laplista = self.driver.find_element_by_id(lokatorok.ul_id).find_elements_by_class_name("card")
        self.kilencesek = 0
        for lap in self.laplista:
            if lap.text[0] == "9":
                self.kilencesek += 1
        return self.kilencesek >= 4


class Test_feladat03():  # Művelet.
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url3)

    def tesztel(self):
        def osszead(a, b):
            return a + b

        def kivon(a, b):
            return a - b

        def szoroz(a, b):
            return a * b

        self.driver.find_element_by_id(lokatorok.button_id).click()
        self.num1 = int(self.driver.find_element_by_id("num1").text)
        self.num2 = int(self.driver.find_element_by_id("num2").text)
        self.num3 = int(self.driver.find_element_by_id("num3").text)
        self.op1 = self.driver.find_element_by_id("op1").text
        self.op2 = self.driver.find_element_by_id("op2").text
        if self.op2 == "*":
            self.c = szoroz(self.num2, self.num3)
            if self.op1 == "+":
                self.eredmeny = osszead(self.num1, self.c)
            elif self.op1 == "-":
                self.eredmeny = kivon(self.num1, self.c)
            else:
                self.eredmeny = szoroz(self.num1, self.c)
        else:
            if self.op1 == "+":
                self.c = osszead(self.num1, self.num2)
            elif self.op1 == "-":
                self.c = kivon(self.num1, self.num2)
            else:
                self.c = szoroz(self.num1, self.num2)
            if self.op2 == "+":
                self.eredmeny = osszead(self.c, self.num3)
            else:
                self.eredmeny = kivon(self.c, self.num3)
        return str(self.eredmeny) == self.driver.find_element_by_id(lokatorok.result_id).text


class Test_feladat04():  # Művelet.
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)

    def tesztel(self, a, b, c, d, e, f):
        self.driver.get(lokatorok.url4)
        self.username = self.driver.find_element_by_id(lokatorok.username)
        self.password = self.driver.find_element_by_id(lokatorok.password)
        self.submitgomb = self.driver.find_element_by_xpath(lokatorok.submitgomb)
        self.letter = self.driver.find_element_by_id(lokatorok.letter)
        self.capital = self.driver.find_element_by_id(lokatorok.capital)
        self.number = self.driver.find_element_by_id(lokatorok.number)
        self.length = self.driver.find_element_by_id(lokatorok.length)
        self.username.clear()
        self.username.send_keys(a)
        self.password.clear()
        self.password.send_keys(b)
        self.submitgomb.click()
        time.sleep(2)
        if c == "":
            return self.driver.find_element_by_id(lokatorok.titletext).text == "404: Not Found"
        else:
            log = self.letter.get_attribute("class") == c
            log = log and self.capital.get_attribute("class") == d
            log = log and self.number.get_attribute("class") == e
            log = log and self.length.get_attribute("class") == f
            return log


class Test_feladat05():  # Művelet.
    def __init__(self):
        self.options = Options()
        self.options.headless = True
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(lokatorok.url5)

    def tesztel(self):
        self.nevek = self.driver.find_element_by_id(lokatorok.sorozat).find_elements_by_tag_name("li")
        self.lista = []
        for nev in self.nevek:
            self.lista.append(nev.text)
        for self.listaelem in self.lista:
            if self.listaelem == self.listaelem.upper():
                self.listaelem = self.listaelem.capitalize()
                self.driver.find_element_by_id(lokatorok.inputmezo).send_keys(self.listaelem)
                self.driver.find_element_by_id(lokatorok.button_id).click()
                break
        return self.driver.find_element_by_id(lokatorok.result_id).text == "Eltaláltad."

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def add_hozza(a):
    buttons = driver.find_element_by_id(a).find_elements_by_tag_name("button")
    return buttons


url = "https://witty-hill-0acfceb03.azurestaticapps.net/imdb_guessmovie.html"
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get(url)

radio_us = driver.find_element_by_id("startScreen").find_elements_by_class_name("country")


gombok = []
sorok = ["row0", "row1", "row2", "row3"]
for sor in sorok:
    gombok.extend(add_hozza(sor))
probak = []
strikek = ["strike0", "strike1", "strike2", "strike3"]
for strike in strikek:
    probak.append(driver.find_element_by_id(strike))

nextgomb = driver.find_element_by_id("confirmNext")


def test_01():
    log = True
    for proba in probak:
        log = log and proba.get_attribute("style") == ""
    for gomb in gombok:
        log = log and gomb.get_attribute("style") == ""
    assert log


def test_02():
    betuk = ["M", "N", "T", "O", "E"]
    for r in radio_us:
        if r.get_attribute("value") == "us":
            r.click()
            break
    time.sleep(4)
    log = True
    for betu in betuk:
        billentyu = driver.find_element_by_id(betu)
        billentyu.click()
        time.sleep(0.9)
        log = log and billentyu.get_attribute("style") == "background: green; transform: scale(1, 1);"
    log = log and nextgomb.text.find("Well Done!") > -1
    nextgomb.click()
    assert log

def test_03():
    betuk = ["1", "2", "3", "4"]
    time.sleep(4)
    log = True
    for betu in betuk:
        billentyu = driver.find_element_by_id(betu)
        billentyu.click()
        time.sleep(0.9)
        log = log and  billentyu.get_attribute("style") == "background: red; transform: scale(1, 1);"
    time.sleep(3)
    nextgomb = driver.find_element_by_id("confirmNext")
    log = log and nextgomb.text.find("Well Done!") == -1
    assert log

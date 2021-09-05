from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = "https://witty-hill-0acfceb03.azurestaticapps.net/caesar.html"
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.get(url)

adatlista = [["abcd", "26\t", "abcd"], ["abcd", "2\t", "cdef"], ["cdef", "-2\t", "abcd"]]
szovegmezo = driver.find_element_by_id("cypher")
eltolasmezo = driver.find_element_by_id("offset")
eredmenymezo = driver.find_element_by_id("finish")


def ellenoriz(a):
    szovegmezo.clear()
    szovegmezo.send_keys(a[0])
    eltolasmezo.clear()
    eltolasmezo.send_keys(a[1])
    return eredmenymezo.get_attribute("value") == a[2]


def test_01():
     assert ellenoriz(adatlista[0])


def test_02():
    assert ellenoriz(adatlista[1])


def test_03():
    assert ellenoriz(adatlista[2])
    driver.close()


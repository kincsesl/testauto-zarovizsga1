import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
url = "https://witty-hill-0acfceb03.azurestaticapps.net/bowling-scorecard.html"
driver.get(url)

frame_ek = []
markerlista = []
markertextlista = ['1', '6', '15', '21', '28', '36', '45', '55', '65', '4510X101010']
fr = 10
for i in range(fr):
    frame_ek.append(driver.find_element_by_id("frame" + str(i + 1)))
    markerlista.append(driver.find_element_by_id("marker" + str(i)))

buttonok = driver.find_element_by_id("buttons").find_elements_by_tag_name("button")

guritasok = [0, 1, 2, 3, 4, 5, 6, 0, 7, 0, 8, 0, 9, 0, 9, 1, 10, 10, 0, 0]
rosszguritasok = [6, 5]

frameertek = ['0,1', '2,3', '4,5', '6,0', '7,0', '8,0', '9,0', '9,/', 'X', 'X,0']
# frameertek = ["0,1","2,3","4,5","6,0","7,0","8,0","9,0","X","X","0,0"] Legyen inkább az előző, az legalább jó.


def test_01():
    log = True
    for frame in frame_ek:
        log = log and frame.text == ""
    for marker in markerlista:
        log = log and marker.text == ""
    assert log


def test_02():
    tenyleges = []
    osszegek = []
    for guritas in guritasok:
        buttonok[guritas].click()
    for frame in frame_ek:
        tenyleges.append(frame.text)
    for marker in markerlista:
        osszegek.append(marker.text)
    log = tenyleges == frameertek
    log = log and osszegek == markertextlista
    assert log


def test_03():
    driver.refresh()
    buttonok = driver.find_element_by_id("buttons").find_elements_by_tag_name("button")
    time.sleep(1)
    for guri in rosszguritasok:
        buttonok[guri].click()
    assert driver.find_element_by_id("comments").text == "Invalid Roll - there are only ten pins!"




import time

import randomstring
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def test_01():
    options = Options()
    # options.headless = True
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    url = "https://witty-hill-0acfceb03.azurestaticapps.net/input-pattern.html"
    driver.get(url)

    inputmezo = driver.find_element_by_xpath("/html/body/input[5]")

    betuk = {"A", "B", "C", "D", "E", "F", "G"}

    sztring = randomstring.veletlen("0[1-5],a[2],A[1-15],&[3]", True)
    sztring_ki = ""

    for i in range(len(sztring)):
        b = sztring[i]
        if b in betuk:
            sztring_ki += b

    # print(sztring, sztring_ki)
    inputmezo.send_keys(sztring)
    time.sleep(1)
    # print(inputmezo.get_attribute("value"))
    assert inputmezo.get_attribute("value") == sztring_ki

    driver.close()

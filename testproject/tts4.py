from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import randomstring
import lokatorok
import osztalyok
from selenium.webdriver.support.ui import Select

feladat02 = osztalyok.Test_feladat02()

assert feladat02.test_tesztel()

feladat02.driver.close()
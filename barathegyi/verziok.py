from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
# options.headless = True
driver = webdriver.Chrome(options=options)
driver.get("https://www.browserstack.com/screenshots")

linkek = driver.find_elements_by_class_name("version")
linkek.append(driver.find_elements_by_class_name("pull-left version"))

print(len(linkek))
with open("linkek.txt", "w") as file:
    for link in linkek:
        s = link.get_attribute("os") + "\t" + link.get_attribute(
            "os_version") + "\t" + link.get_attribute("browser") + "\t" + link.text + "\n"
        file.write(s)

driver.close()

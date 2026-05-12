from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

options = Options()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122 Safari/537.36"
)

service = Service("your chromedriver location")
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")
time.sleep(2)

try:
    driver.find_element(By.XPATH, "//button//div[text()='I agree' or text()='Accept all']").click()
except:
    pass

time.sleep(2)

search = driver.find_element(By.NAME, "q")
search.click()
time.sleep(1)

search.send_keys("your category")
time.sleep(1)

search.send_keys(Keys.ENTER)
time.sleep(2)

soup = BeautifulSoup(driver.page_source, "html.parser")
name_list = soup.find_all("h3")

with open("names.txt", "a", encoding="utf8") as f:
    for name in name_list:
        f.write(name.text.strip())
        f.write("\n")

driver.quit()
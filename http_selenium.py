from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# webdriver 객체를 생성해서, 브라우저 자체를 제어한다.
import json
with open('./secrets.json', "r") as json_file:
    secrets = json.load(json_file)


browser = webdriver.Chrome('./chromedriver')
# print("Webdriver Object", browser)
browser.get('https://sell.smartstore.naver.com/#/login')

element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, "loginId"))
)  # wait for page to load, so element with ID 'username' is visible

id_box = browser.find_element(By.XPATH, "//input[@id='loginId']")
password_box = browser.find_element(By.XPATH, "//input[@id='loginPassword']")
id_box.send_keys(secrets['id'])
password_box.send_keys(secrets['password'])
browser.find_element_by_id('loginButton').click()

element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located(
        (By.NAME, "naverpay-salesinfo"))
)  # wait for page to load, so element with ID 'username' is visible
browser.get(
    'https://sell.smartstore.naver.com/#/naverpay/sale/delivery?summaryInfoType=DELIVERY_READY')

element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "tui-grid-table"))
)
print('a')
orders = browser.find_elements_by_xpath(
    "//table[@class='tui-grid-table']/tbody/tr")
for order in orders:
    order.find_elements_by_xpath("//td[2]/a").click()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import locale

options = webdriver.ChromeOptions()
cService = webdriver.ChromeService(executable_path="C:\Program Files (x86)\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=cService)

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

driver.get("https://www.fromjapan.co.jp/en/member/login")

driver.implicitly_wait(30)
loginEmail = driver.find_element("name", "login")
loginEmail.send_keys("<insert account email>")  # account email for login

loginPassword = driver.find_element("name", "passwd")
loginPassword.send_keys("<insert password>")  # account password for login

loginPassword.send_keys(Keys.ENTER)
savedBid = int(0)

for i in range(100):

    driver.get(
        "https://www.fromjapan.co.jp/japan/en/auction/yahoo/input/q1124064848/")  # example. replace with auction listing of choise
    time.sleep(2)

    current_bid = driver.find_element(By.XPATH,
                                      "//*[contains(@class,'text-2xl lg:text-4xl text-danger font-semibold')]")  # locate current bid amount
    stringBid = current_bid.text

    numberBid = int(stringBid.replace(',', ''))
    print(numberBid)
    limit = int(1000)

    time_left = driver.find_element(By.XPATH,
                                    "//*[contains(@class,'text-xl font-semibold')]")  # locate time left on the bid
    stringTimeLeft = time_left.text
    numtimeLeft = int(stringTimeLeft.replace(':', ''))

    print(numtimeLeft)
    timeBidStartAt = 500
    #
    if (savedBid != numberBid):
        bid_price = driver.find_element(By.XPATH,
                                        "//*[contains(@class,'vs-inputx vs-input--input normal hasValue')]")  # locate entry field for bid
        bid_price.send_keys(Keys.CONTROL, "a");
        bid_price.send_keys(Keys.DELETE)

        time.sleep(2)
        savedBid = int(numberBid + 20)  # increase bid by 20 yen
        bid_price.send_keys(savedBid)

        bid_button = driver.find_element(By.CLASS_NAME, "fj-button")  # locate the 'Place Bid' button

        if numberBid <= limit:
            bid_button.click()
            driver.implicitly_wait(2)

            place_bid = driver.find_element(By.CSS_SELECTOR,
                                            "button[type='submit']")  # second 'Place Bid' button on the confirmation page

            place_bid.click()
            driver.implicitly_wait(10)
            confirm = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div/div[5]/div[2]/button')
            confirm.click()
            time.sleep(15)
            driver.get("https://www.fromjapan.co.jp/japan/en/auction/yahoo/input/q1124064848/")
        else:
            exit()
    else:
        driver.refresh()

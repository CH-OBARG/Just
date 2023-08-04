from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return(math.log(abs(12 * math.sin(x))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    btn = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    btn.click()
    x = browser.find_element(By.ID, "input_value").text
    browser.find_element(By.ID, "answer").send_keys(calc(int(x)))
    browser.find_element(By.ID, "solve").click()

    time.sleep(5)

finally:
    time.sleep(10)
    browser.quit()


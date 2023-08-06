from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestUni(unittest.TestCase):
    def test_first(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys("a")
        browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input").send_keys("b")
        browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input").send_keys("c")
        browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input").send_keys("1")
        browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input").send_keys("1a")
        browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()

    def test_second(self):
        browser = webdriver.Chrome()
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[1]/input").send_keys("a")
        browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[2]/input").send_keys("b")
        browser.find_element(By.XPATH, "/html/body/div/form/div[1]/div[3]/input").send_keys("c")
        browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[1]/input").send_keys("1")
        browser.find_element(By.XPATH, "/html/body/div/form/div[2]/div[2]/input").send_keys("1a")
        browser.find_element(By.CSS_SELECTOR, "body > div > form > button").click()


if __name__ == "__main__":
    unittest.main()

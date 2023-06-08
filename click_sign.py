from selenium.webdriver.common.by import By
import time

def sign(browser, web):
    browser.get(web)
    time.sleep(8)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/main/div[1]/div[2]/div[2]/button").click()
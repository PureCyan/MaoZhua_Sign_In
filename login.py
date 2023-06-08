from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time, random

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')

def login(web, pwd, acc): 
    s = Service(executable_path=r"/usr/local/bin/chromedriver")
    browser = webdriver.Chrome(service=s, options=chrome_options)
    browser.get(str(web))
    time.sleep(5)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/div[1]/button[1]").click()
    time.sleep(10)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/form/div[2]/label[2]/input").send_keys(acc)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/form/div[2]/label[5]/input").send_keys(pwd)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[2]/div/div/div/form/div[2]/div[2]/button").click()
    return browser
    


from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
import time, requests, re, random

def get_links(web):
    links = []
    web_data = requests.get(web).text
    soup = bs(web_data, 'lxml')
    links = []
    main_tag = soup.find('main')
    if main_tag:
        ul_tag = main_tag.find('ul')
        if ul_tag:
            for li in ul_tag.find_all('li'):
                match = re.search(r'href=[\'"]?([^\'" >]+)', str(li))
                if match:
                    links.append(match.group(1))
    return links

def random_links(links):
    random_element = random.choice(links)
    links_data = requests.get(random_element).text
    #links_data = requests.get(links).text
    soup = bs(links_data, 'lxml')
    links = []
    div_tag = soup.find('div', {'id': 'post-list'})
    if div_tag:
        for li in div_tag.find_all('li'):
            match = re.search(r'href=[\'"]?([^\'" >]+)', str(li))
            if match:
                links.append(match.group(1))
    print(links)    

def comment(browser, web):
    browser.get(web)
    time.sleep(8)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/div/div[2]/div/div[3]/div[2]/div[2]/textarea").send_keys("好")
    time.sleep(8)
    browser.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/div/div[2]/div/div[3]/div[3]/div[2]/button[2]").click()
    time.sleep(3)
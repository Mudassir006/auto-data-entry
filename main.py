import time

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_driver_path = "/Users/Dell/Desktop/Chrome/chromedriver"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service= service)

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}



response = requests.get("https://www.zillow.com/la/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A33.83057698413483%2C%22east%22%3A-87.08324304687498%2C%22south%22%3A28.000548555515138%2C%22west%22%3A-95.71849695312498%7D%2C%22mapZoom%22%3A7%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A25%2C%22regionType%22%3A2%7D%5D%7D",headers=header)

data = response.text
c = []
k = []

soup = BeautifulSoup(data,'html.parser')
for add in soup.findAll('address'):
    x= add.text
    c.append(x)
print(c)

all_price_elements = soup.select(".kJFQQX")
all_prices = [price.get_text().split("+")[0] for price in all_price_elements if "$" in price.text]
print(all_prices)
all_link_elements = soup.select(".epgJFL a")

all_links = []
for link in all_link_elements:
    href = link["href"]
    if "http" not in href:
        all_links.append(f"https://www.zillow.com{href}")
    else:
        all_links.append(href)

print(all_links)



for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLScghszKVC59EbSMyqtoHnUy07w0Pn8Hsb9G7yCzC8I3kd5SLQ/viewform")
    x = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    x2 = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    x3 = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    y = driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    x.send_keys(c[n])
    x2.send_keys(all_prices[n])
    x3.send_keys(all_links[n])

    y.click()
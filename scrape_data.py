import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-dev-shm-usage') # use tmp and write to disk instead of use memory

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = 'https://www.lionsclub-mettmann-wuelfrath.de/aktivitaeten/adventskalender_gewinnerlose.html'

driver.get(url)

soup = BeautifulSoup(driver.page_source, 'lxml')

tables = soup.find_all("div", {"class": "com-content-category-blog__items blog-items boxed"})

for table in tables:
    output_data = str(table.getText())

#print(mail_input)

driver.quit

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

url = "https://gyms.vertical-life.info/intellighenzia-project-asd/checkins#/service/custom-1/74/2023-11-23"

#opzioni del browser
chrome_options = Options()
chrome_options.add_argument("--headless") #serve per far capire al browser che non richiediamo la visualizzazione di quest'ultimo
#creazione del driver
driver = webdriver.Chrome(service=Service(PATH), options=chrome_options)

time.sleep(2)

html = BeautifulSoup(page.text, 'html')

liberi = html.find_all('div', class_='row align-items-center')

if liberi:
        for libero in liberi:
            print(libero)
else:
        print("No elements found with the specified class.")


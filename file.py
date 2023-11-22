from bs4 import BeautifulSoup
import requests

url = "https://gyms.vertical-life.info/intellighenzia-project-asd/checkins#/service/custom-1/74/2023-11-23"

page = requests.get(url)

html = BeautifulSoup(page.text, 'html')

liberi = soup.find_all('Prenota', class_='card')

for libero in liberi:
    print(libero)

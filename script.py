from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

# Impostazioni per il browser
chrome_path = '/percorso/verso/chromedriver'  # Inserisci il percorso del tuo chromedriver
url = 'https://www.example.com'  # URL del sito da cui vuoi estrarre le informazioni

# Configurazione del browser con Selenium
service = Service(chrome_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

# Estrarre il codice HTML della pagina con Selenium
html = driver.page_source

# Chiudere il browser dopo aver ottenuto il codice HTML
driver.quit()

# Analizzare il codice HTML con BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Trovare e stampare il titolo della pagina
title = soup.find('title')
if title:
    print("Titolo della pagina:", title.text)
else:
    print("Nessun titolo trovato.")

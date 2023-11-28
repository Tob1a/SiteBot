from selenium.webdriver import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class setup():
    def __init__(self, PATH):
        self.PATH=PATH
        #opzioni del browser
        chrome_options = Options()
        chrome_options.add_argument("--headless") #serve per far capire al browser che non richiediamo la visualizzazione di quest'ultimo
        #creazione del driver
        self.driver = webdriver.Chrome(service=Service(self.PATH), options=chrome_options)
        return self.driver
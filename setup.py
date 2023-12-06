from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import platform




class setup():

    def get_PATH():
        system = platform.system()
        architecture = platform.machine()
        if system == 'Windows':
            return "/drivers/chromedriver.exe"
        elif system == 'Linux':
            return "/drivers/chromedriver_linux"
        elif system == 'Darwin': #darwin e;' per macos
            if architecture == 'arm64':
                return "/drivers/chromedriver_mac_arm"
            else:
                return "/drivers/chromedriver_mac_x64"
        else:
            raise Exception("Il sistema non e' supportato")

        


    def __init__(self):
        self.PATH= setup.get_PATH()
        #opzioni del browser
        chrome_options = Options()
        chrome_options.add_argument("--headless") #serve per far capire al browser che non richiediamo la visualizzazione di quest'ultimo
        #creazione del driver
        self.driver = webdriver.Chrome(service=Service(self.PATH), options=chrome_options)
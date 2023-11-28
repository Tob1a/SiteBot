from setup import setup
from search import search

url = "https://gyms.vertical-life.info/intellighenzia-project-asd/checkins#/service/custom-1/74/2023-11-23"
PATH = "/home/tobu/Scaricati/chromedriver-linux64"
OrarioMax = ""
OrarioMin = ""

driver = setup(PATH)
    

liberi = search(url,OrarioMax,OrarioMin,driver)



if liberi:
        for libero in liberi:
            print(libero)
else:
        print("No elements found with the specified class.")


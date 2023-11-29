from setup import setup
from search import search
from output import output
import time
import threading

class sitebot:

    def __init__(self) -> None:
        pass

    def sitebot(self):

        url = "https://gyms.vertical-life.info/intellighenzia-project-asd/checkins#/service/custom-1/74/2023-11-30"
        PATH = "/home/tobu/Scaricati/chromedriver-linux64/chromedriver"
        OrarioMax = 0
        OrarioMin = 460
        news=["","","","","","","","","","",""]

        while True:


            setup_istance = setup(PATH)


            liberi = search(url,OrarioMax,OrarioMin,setup_istance.driver).liberi


            ciao=output(liberi,news)
            news=ciao.ottieni_array()

            time.sleep(60)

            setup_istance.driver.quit()





    def main(self):
        
        thread = threading.Thread(target=self.sitebot)
        thread.daemon = True
        thread.start()
        


        while True:
            user_input = input("Inserisci 'ciao' per interrompere il loop: ")
            if user_input.lower() == 'ciao':
                break
        

        #fine main



if __name__ == "__main__":
    sb = sitebot()
    sb.main()


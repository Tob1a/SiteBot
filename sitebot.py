from setup import setup
from search import search
from output import output
from inputdata import inputdata
import time
import threading

#per il requirements.txt usare il comando pipreqs /home/tobu/Documenti/GitHub/SiteBot/


class sitebot:

    def __init__(self) -> None:
        pass
 
    def sitebot(self,url,OrarioMax,OrarioMin,email,password):
        
        self.url = url
        self.OrarioMax = OrarioMax
        self.OrarioMin = OrarioMin
        self.email = email
        self.password = password

        self.url = "https://gyms.vertical-life.info/intellighenzia-project-asd/checkins#/service/custom-1/74/2023-11-30"
        PATH = "/home/tobu/Scaricati/chromedriver-linux64/chromedriver"
        self.OrarioMax = 0
        self.OrarioMin = 460
        news=["","","","","","","","","","",""]
        self.email="@gmail.com"
        self.password=""

        




        while True:


            setup_istance = setup(PATH)


            liberi = search(self.url,self.OrarioMax,self.OrarioMin,setup_istance.driver).liberi


            ciao=output(liberi,news,self.email,self.password)
            news=ciao.ottieni_array()

            time.sleep(60)

            setup_istance.driver.quit()





    def main(self):
        Input = inputdata()
        url, OrarioMax, OrarioMin, email, password = Input.get_input()
        
        thread = threading.Thread(target=self.sitebot(url,OrarioMax,OrarioMin,email,password))
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


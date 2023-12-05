from typing import Any


class inputdata:
    def __init__(self):
        try:
            self.url = input("Inserisci l'url del sito:\n")
            self.PATH = input("\nInserisci il percorso per il file (es. /home/tobu/Scaricati/chromedriver-linux64/chromedriver). Sei tobia scrivi d e sei apposto")
            if self.PATH == "d":
                self.PATH = "/home/tobu/Scaricati/chromedriver-linux64/chromedriver"
            self.OrarioMax = input("\nInserisci i pixel per spostare l'orario massimo della prenotazione (solitamente 0):\n")
            self.OrarioMax=int(self.OrarioMax)
            self.OrarioMin = input("\nInserisci i pixel per spostare l'orario minimo della prenotazione (solitamente 460):\n")
            self.OrarioMin=int(self.OrarioMin)
            self.email = input("\nInserisci la tua Gmail (es pippo.pluto@gmail.com):\n")
            if not (self.email.endswith("@gmail.com")):
                print("Si e' verificato un problema nell'inserimento della mail")
                exit(1)
            self.password = input("\nInserisci la tua password (vedi come su github):")
        except ValueError as e:
            print("Si e' verificato un problema nell'inserimento dati ", e)
            exit(1)

    def get_input(self):
        return self.url, self.OrarioMax, self.OrarioMin, self.email, self.password
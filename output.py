from mail import mail

class output():
    def __init__(self,liberi,news,email,password):
        self.liberi=liberi
        self.news=news
        self.frase_da_escludere = "Tutto esaurito"

        if self.liberi:
            i=-1
            for libero in self.liberi:  
                i=i+1 
                if self.frase_da_escludere not in libero.text:
                    print(libero.text)
                    if self.news[i] != libero.text:
                        self.news[i] = libero.text
                        mail(email,password,libero.text)
                        print("c'e' qualcosa di nuovo")
        else:
            print("No elements found with the specified class.")


    def ottieni_array(self):
        return self.news
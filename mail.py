from email.message import EmailMessage
import ssl
from smtplib import SMTP_SSL

class mail():
    
    def __init__(self,indirizzo,password,contenuto) -> None:
        self.email_reciver=indirizzo
        self.subject="SiteBot'"
        self.body="""
        Ciao, hai delle novita

        """+contenuto

        #creazione em della mail
        em=EmailMessage()
        em['From'] = indirizzo
        em['To'] = self.email_reciver
        em['subject'] = self.subject
        em.set_content(self.body)



        #creazione dell ssl per la connessione
        context = ssl.create_default_context()

        #connessione
        with SMTP_SSL('smtp.gmail.com',465, context=context) as smtp:
            smtp.login(indirizzo,password)
            smtp.sendmail(indirizzo,self.email_reciver,em.as_string())
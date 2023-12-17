# Controlla la Disponibilità di Posti in una Palestra di Arrampicata

## Descrizione
Questo programma, realizzato in Python, consente di verificare la disponibilità dei posti in una palestra di arrampicata specifica. Utilizza la libreria Selenium per effettuare lo scraping (raschiamento) del sito web della palestra, controllando costantemente lo stato della prenotazione dei posti e notificando all'utente quando si liberano posti disponibili.

## Funzionalità
- **Controllo della Disponibilità:** Il programma effettua automaticamente una scansione del sito web della palestra per controllare la disponibilità dei posti utilizzando Selenium.
- **Notifiche:** Quando vengono rilevati posti disponibili, il programma invia notifiche all'utente per informarlo.

## Requisiti
- Python 3.x
- Dipendenze esterne elencate nel file `requirements.txt`, tra cui la libreria `Selenium`.
- Scarica il corretto `chromedriver` per la tua versione di Chrome utilizzando [questo link](https://googlechromelabs.github.io/chrome-for-testing/).
  - Sposta il file scaricato nella cartella `drivers`.
  - Rinomina il file come `chromedriver_nomedelsistemaoperativochestateusando`.

## Installazione e Utilizzo
1. Clona o scarica il repository sul tuo computer.
2. Assicurati di avere Python installato.
3. Installa le dipendenze eseguendo il comando: `pip install -r requirements.txt`.
4. Esegui il programma con il comando: `python sitebot.py`.
5. Segui le istruzioni per configurare il programma inserendo i dati necessari (URL della palestra, dati di accesso, preferenze di notifica, ecc.).
6. Il programma inizierà a monitorare la disponibilità dei posti e ti notificherà in caso di posti disponibili.

## Contributi
Sono benvenuti contributi, suggerimenti e miglioramenti. Sentiti libero di aprire un issue o fare una pull request.

## Attenzione
Questo programma è stato sviluppato per scopi educativi e personali. L'uso di questo software per violare i termini di servizio di qualsiasi sito web è responsabilità dell'utente.

## Autori
- [Tob1a](https://github.com/Tob1a) - Tob1a

---

*Nota:* Sto creando il file avvio.sh che dovrebbe semplificare le cose.

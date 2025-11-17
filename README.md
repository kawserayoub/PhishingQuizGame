# To be Phished or not to be Phished

Ett interaktivt quiz som tränar användare i att upptäcka phishing mejl. Ett tidigare prototyp finns i mappen "ProofOfConcept".
---
### Projektstruktur

```text
├── Final_Project
│   ├── images/         # Bakgrundsbilder och mejlskärmdumpar som visas i quizet
│   ├── data.py         # quiz_data: frågor, alternativ, rätt svar, förklaringar, bildvägar
│   ├── functions.py    # Kärnlogik: initiera quiz, hämta fråga, rätta svar, nollställning
│   └── main.py         # GUI-kod: alla sidor, navigation, knappar och Security Tips-sektionen
├── ProofOfConcept
│   ├── images/           # Bilder från den första prototypen
│   ├── PoC_code.py       # Tidig enkel prototyp av quizet
│   └── PoC_notes.ipynb   # Notebook med anteckningar och experiment
└── README.md
```
----
### Hur du kör projektet:

```bash
cd Final_Project
python main.py
```
----
### Hur du använder applikationen:

1. Läs introduktionen och tryck START
2. Navigera med RETURN och NEXT genom sidorna
3. I quizet: läs scenario, granska mejlbilden och välj mellan alternativen
4. Efter sista frågan visas sitt resultat.
5. Gå vidare till Security tips för se olika central säkerhetsvanor.
6. Använd "Restart" för att börja om eller "Exit" för att avlsuta

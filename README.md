# crawler_advent_lions
wozu dient das ganze?
gewinnspiel losnummern von der lions HP abziehen und per mail versenden - damit muss ich nicht immer die seite besuchen um zu checken ob ich gewonnen habe.

# Setup
creds.py 
--> im main folder erstellen und die relevanten login credentials für google smtp als variablen hinterlegen:
sender_email = "stephanskynet@gmail.com" --> insert your mail
password = "insert_your_password"

scraper.py
--> find all tables on adventskalender_gewinnerlose @lionsclub-mettmann-wuelfrath.de
(https://www.lionsclub-mettmann-wuelfrath.de/aktivitaeten/adventskalender_gewinnerlose.html)

send_mail.py
--> versendet die gescrapten daten aus der scraper.py in kobination mit der creds.py per email 
--> erhalter können hier festegelegt werden

# Nützliche Anleitungen
crawler
https://www.youtube.com/watch?v=xrYDlx8evR0
https://www.youtube.com/watch?v=1PCWwK0AsE0&t=655s

eMail
https://stackoverflow.com/questions/71924634/sending-emails-using-python-smtplib-and-emailmessage

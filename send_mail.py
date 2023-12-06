#external
import smtplib
from email.message import EmailMessage
#internal
import scrape_data
import creds

msg = EmailMessage()
msg.set_content(scrape_data.output_data)

msg['Subject'] = 'Advent-Advent'
msg['From'] = creds.sender_email
msg['To'] = "stephan.juelich.85@gmail.com,lisamarie.juelich@gmail.com"

# Send the message via our own SMTP server.
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(creds.sender_email, creds.password)
server.send_message(msg)
server.quit()

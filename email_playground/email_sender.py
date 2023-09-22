import smtplib
from string import Template
from pathlib import Path

from email.message import EmailMessage

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from']    = ''   # name of the sender
email['to']      = ''   # recipient's email address
email['subject'] = ''   # subject line for the email

email.set_content(html.substitute({'name': 'Chloe'}), 'html')   # body/content of the email

with smtplib.SMTP(host = 'smtp.gmail.com', port = 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('', '')          # your credentials --> ('email', 'password')
    smtp.send_message(email)
    print('Email Sent!')
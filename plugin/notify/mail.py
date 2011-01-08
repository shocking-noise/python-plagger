"""
example

- module: notify.mail
  config:
    from: test@test.com
    to: test@test.com
    subject: test
"""

import smtplib
from email.MIMEText import MIMEText
from email.Utils import formatdate

def create_message(from_addr, to_addr, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()
    return msg

def send(from_addr, to_addr, msg):
    s = smtplib.SMTP()
    s.sendmail(from_addr, [to_addr], msg.as_string())
    s.close()

def mail(config,data):
    msg = create_message(config['from'],config['to'],config['subject'],'\n'.join(data))
    send(config['from'],config['to'],msg)
    return data

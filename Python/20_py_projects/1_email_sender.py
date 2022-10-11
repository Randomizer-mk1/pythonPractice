from email.message import EmailMessage
from app2 import password

import ssl
import smtplib

email_sender = 'kevinkim846@gmail.com'
email_password = password

email_receiver = ''

subject = "Don't fuck with me"
body = """ 

Kill me

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
    smtp.login(user, password)
    smtp.sendmail(from_addr, to_addrs, em.as_string())



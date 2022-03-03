import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg['Subject'] = 'test'
msg['From'] = '7000766645az@gmail.com'
msg['To'] = 'dubeyshivam264@gmail.com'

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login('7000766645az@gmail.com','sxxbrfedfakhlreh')
server.send_message(msg)
server.quit()

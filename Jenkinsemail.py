import smtplib
import ssl

server = smtplib.SMTP.ssl('smtp.gmail.com', 465)

server.starttls()
server.login('7000766645az@gmail.com','sxxbrfedfakhlreh')

server.sendmail('7000766645az@gmail.com',
                 'dubeyshivam264@gmail.com',
                 "hello shivam")

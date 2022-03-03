import smtplib

server = smtplib.SMTP.SSL('smtp.gmail.com', 465)

server.starttls()
server.login('7000766645az@gmail.com','sxxbrfedfakhlreh')

server.sendmail('7000766645az@gmail.com',
                 'dubeyshivam264@gmail.com',
                 "hello shivam")

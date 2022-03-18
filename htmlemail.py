import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd


html = '''
<html>
<head>
<style>
table {
  font-family: arial, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

td, th, td {
  border: 1px solid black;
  text-align: left;
  padding: 8px;
}

tr:nth-child(even) {
  background-color: #dddddd;
}
</style>
</head>
<body>

<h2>IDENTITY DETAILS</h2>

<table>
  <tr>
    <th>Company</th>
    <th>Contact</th>
    <th>Country</th>
  </tr>
  <tr>
    <td>Kpit</td>
    <td>Shivam Dubey</td>
    <td>India</td>
  </tr>
  <tr>
    <td>Kpit</td>
    <td>Jay</td>
    <td>india</td>
  </tr>
  <tr>
    <td>Kpit</td>
    <td>Dharmendra</td>
    <td>India</td>
  </tr>
  <tr>
    <td>Kpit</td>
    <td>Helen Bennett</td>
    <td>UK</td>
  </tr>
</table>

</body>
</html>
    '''


email_from = '7000766645az@gmail.com'
password = 'oznxtbjcriaocrvj'
email_to = 'dubeyshivam264@gmail.com'


date_str = pd.Timestamp.today().strftime('%Y-%m-%d')


email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Report email - {date_str}'


email_message.attach(MIMEText(html, "html"))

email_string = email_message.as_string()


context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
   server.login(email_from, password)
   server.sendmail(email_from, email_to, email_string)

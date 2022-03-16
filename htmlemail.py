
import smtplib, ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
## The pandas library is only for generating the current date, which is not necessary for sending emails
# import pandas as pd

# Define the HTML document
html = '''
   <!DOCTYPE html>
<html>

   <head>
      <title>HTML Tables</title>
   </head>
	
   <body>
      <table border = "1">
         <tr>
            <td>ID 1, shivam</td>
            <td>ID 2, jay</td>
         </tr>
         
         <tr>
            <td>ID 1, rohan</td>
            <td>Id 2, harsh</td>
         </tr>
      </table>
      
   </body>
</html>
    '''

# Set up the email addresses and password. Please replace below with your email address and password
email_from = '7000766645az@gmail.com'
password = 'oznxtbjcriaocrvj'
email_to = 'dubeyshivam264@gmail.com'

# Generate today's date to be included in the email Subject
# date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
# email_message['Subject'] = f'Report email - {date_str}'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
email_message.attach(MIMEText(html, "html"))
# Convert it as a string
email_string = email_message.as_string()

# Connect to the Gmail SMTP server and Send Email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
   server.login(email_from, password)
   server.sendmail(email_from, email_to, email_string)

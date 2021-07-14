''' This programs can send Email to required persons with attachments as well...'''
import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = "santiwartest2603@gmail.com"
receiver = "tiwari.sandarbh2603@gmail.com"
# password = input("Please enter password of your Email to login and send the email: ")

message = MIMEMultipart("alternative")
message["Subject"] = "This is a MIMEMultipart Alternative Test Email"
message["From"] = sender
message["To"] = receiver

text = """ Hi, How are you? \n Hope you are doing good amid this Covid-19. """
html = """\
<html>
    <head>
        <style type="text/css">
            @import url('https://fonts.googleapis.com/css2?family=Montserrat&family=Oswald&display=swap');
            h1,h2,h3,h4,h5,h6 {font-family: 'Oswald', sans-serif;}
            p, a, li, ul, ol {font-family: 'Montserrat', sans-serif;}
        </style>
    </head>
    <body>
        <h2 style="color : #dc143c;">Hi Sandarbh!</h2><br>
            <p>This is a test email from Python Script. Please do not revert back.</p>
    </body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

def sendEmail():
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, password)
        server.sendmail(
            sender, receiver, message.as_string()
        )

if __name__ == '__main__':
    password = input("Please enter password of your Email to login and send the email: ")
    sendEmail()
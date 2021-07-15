import smtplib, ssl, imghdr
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendPlaintextMail(senderID, receiverID, userCredentials):
    ''' this function sends a simple text body email '''
    message = input("Please Enter your message below: \n")
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(senderID, userCredentials)
            server.sendmail(senderID, receiverID, message)
    except Exception as e:
        print(e)
        print("Sorry, Some Error Occurred. Please Try again later...")

def sendHtmlMail(senderID, receiverID, userCredentials, mailSub):
    ''' this function attaches HTML code as payload and send the mail '''
    message = MIMEMultipart("alternative")
    message['Subject'] = mailSub
    message['From'] = senderID
    message['To'] = receiverID

    htmlPayload = """\
        <!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<style>
            .main-container{
                display: flex;
                justify-content: center;
                border: 2px dashed #008080;
                padding: 10px;
            }
			.card {
                border: 4px solid #DC143C;
				box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
				transition: 0.3s;
				width: auto;
			}
			
			.card:hover {
				box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
			}

			.container {
				padding: 2px 16px;
			}

            .btn-div{
                display: flex;
                justify-content: center;
            }

            .btn {
                border: 4px solid black;
                background-color: white;
                color: black;
                padding: 14px 28px;
                font-size: 16px;
                cursor: pointer;
                border-radius: 5px;
            }

            .success {
                border-color: #04AA6D;
                color: green;
            }

            .success:hover {
                background-color: #04AA6D;
                color: white;
            }
		</style>
	</head>
	<body>
		<div class="main-container">
            <div class="card">
			    <img src="https://raw.githubusercontent.com/dev-sandarbh/PythonOneDayBuilds/master/avatar-john.png" alt="Avatar" style="width:100%">
			    <div class="container">
				    <h4><b>John Doe</b></h4>
				    <p>Architect & Engineer</p>
			    </div>
		    </div>
        </div>
        <br><hr><br>
        <div class="btn-div">
            <button class="btn success">Check John's Profile</button>
        </div>
	</body>
</html>
        """
    # attaching HTML Payload
    message.attach(MIMEText(htmlPayload, "html"))

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(senderID, userCredentials)
            server.sendmail(senderID, receiverID, message.as_string())
    except Exception as e:
        print(e)
        print("Sorry, Some Error Occurred. Please Try again later...")

def sendAttachmentMail():
    pass

if __name__ == "__main__":
    sender = input("Please Enter Valid Sender Email Address: ")
    receiver = input("Please Enter Valid Receiver Email Address: ")
    password = input("Please Enter Credentials to LogIn and Send Email: ")
    subject = input("Please Enter the Subject of the mail: ")
    print("This Service offers you 3 Variants: \n1. Send a Plain Text Mail \n2. Send HTML Customized Email \n3. Send Email With Attachments Such as .pdf, .txt, or image files")
    ch = int(input("Please Enter your Choice: "))
    if ch == 1:
        sendPlaintextMail(sender, receiver, password, subject)
    elif ch ==2:
        sendHtmlMail(sender, receiver, password, subject)
    elif ch == 3:
        sendAttachmentMail(sender, receiver, password, subject)
    else:
        print("Wrong Service Chosen. Please Enter Correct Service Number and Try Again.!")
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os


def mailern():
    fromaddr = "akash.roshan@iffort.com"
    toaddr = "vittu.amit@gmail.com"
    #recipients = 'vittu.amit@gmail.com'
    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr
    #msg['To'] = ", ".join(recipients)

    # storing the subject
    msg['Subject'] = "Canonizer3 report"

    # string to store the body of the mail
    body = "Hello here is the Canonizer3 report"

    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))


    #filename = "test/TestResults___main__.TestPages_2022-09-06_15-54-23.html"
    filename = ("t.txt")
    print(filename)
    #attachment = open("test/TestResults___main__.TestPages_2022-09-06_15-54-23.html", "rb")
    attachment = open(filename, "rb")

    # instance of MIMEBase and named as p
    p = MIMEBase('application', 'octet-stream')

    # To change the payload into encoded form
    p.set_payload(attachment.read())

    # encode into base64
    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename= %s" % filename)

    # attach the instance 'p' to instance 'msg'
    msg.attach(p)

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()
    #s.ehlo("helo")
    passw = "password"
    # Authentication
    s.login(fromaddr, passw)

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)
    #s.sendmail(fromaddr, recipients, text)

    # terminating the session
    s.quit()

if __name__ == "__main__":
    mailern()

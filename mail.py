def emailv(hname,vname,vphone,vmail,intime,outtime):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
   # from message import *

    fromaddr = "email from which mail has to be sent"
    toaddr = vmail

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Visitor Information"

    # string to store the body of the mail
    body = "Visitor's Name: "+ vname + "\nPhone Number: "+ str(vphone) + "\nVisitor's Email: "+ vmail + "\nIntime: " + str(intime) + "\nOut time: " + str(outtime[0][0]) + "\nHost: "+ str(hname)
    #text = body.astype(str)
    # attach the body with the msg instance
    msg.attach(MIMEText(body , 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "password")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()
    print("Mail sent to the Visitor.")
    #vmessage(body,vphone)   # to send sms to the visitor uncomment this line.
    return 0

def emailh(hmail,vname,vphone,vmail,intime,hphone):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.base import MIMEBase
    from email import encoders
    #from message import *

    fromaddr = "email from which mail has to be sent"
    toaddr = hmail

    # instance of MIMEMultipart
    msg = MIMEMultipart()

    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Visitor Information"

    # string to store the body of the mail
    body = "Visitor's Name: "+ vname + "\nPhone Number: "+ str(vphone) + "\nVisitor's Email: "+ vmail + "\nIntime: " + str(intime)
    #text = body.astype(str)
    # attach the body with the msg instance
    msg.attach(MIMEText(body , 'plain'))

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    s.login(fromaddr, "password")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()
    print("Mail sent to the Host")
    hmessage(body, hphone)         # to send sms to the host uncomment this line.

    return 0

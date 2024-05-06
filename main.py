import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, to_email):
    sender_email = "support@learnfinity.co.uk"
    sender_password = "qyignwqgadmanbbw"

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = to_email
    message['Subject'] = subject


    # The body and the attachments for the mail
    message.attach(MIMEText(body, 'plain'))
    # Create SMTP session for ending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587)    # use Gmail with port
    session.starttls()  # enable security
    session.login(sender_email, sender_password)  # login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_email, to_email, text)
    session.quit()
    print('Mail sent')

# Example usage
send_email('hello from python', 'This is a test email', 'Ahmedhersi717@gmail.com')








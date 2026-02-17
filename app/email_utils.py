from dotenv import load_dotenv
load_dotenv()

# used to send email via SMTP
import smtplib

# create email format
from email.message import EmailMessage

# read data from env file
import os

def send_reset_email(to_email,token):
    msg = EmailMessage()
    msg.set_content(f"Reset your password by using this token :{token}")
    msg["Subject"] = "Password Reset"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = to_email
    with smtplib.SMTP_SSL("smtp.gmail.com",465) as server:
        print("EMAIL_USER:", os.getenv("EMAIL_USER"))
        print("EMAIL_PASS:", os.getenv("EMAIL_PASS"))
        server.login(os.getenv("EMAIL_USER"),os.getenv("EMAIL_PASS"))
        server.send_message(msg)
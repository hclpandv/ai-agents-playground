import smtplib
from email.mime.text import MIMEText
from config import EMAIL_SENDER, EMAIL_RECEIVER, EMAIL_PASSWORD

def send_email(body):
    msg = MIMEText(body)
    msg["Subject"] = "📰 Daily India News Digest (vikiCustomAiAgent)"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
    server.quit()

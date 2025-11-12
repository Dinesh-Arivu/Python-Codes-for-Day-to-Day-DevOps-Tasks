import shutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

THRESHOLD = 80
EMAIL_TO = "admin@example.com"
EMAIL_FROM = "devops@example.com"
SMTP_SERVER = "localhost"  # Change if using external SMTP

# Get disk usage
total, used, free = shutil.disk_usage("/")
usage = (used / total) * 100

print(f"Current disk usage: {usage:.2f}%")

if usage > THRESHOLD:
    subject = "Disk Usage Alert"
    body = f"Warning! Disk usage is at {usage:.2f}% on root (/)."
    
    # Build email
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    # Send email
    try:
        with smtplib.SMTP(SMTP_SERVER) as server:
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        print("Alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

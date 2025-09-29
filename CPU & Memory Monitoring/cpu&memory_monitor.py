import psutil
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80

# Email settings
EMAIL_TO = "admin@example.com"
EMAIL_FROM = "devops@example.com"
SMTP_SERVER = "localhost"  # Change if using external SMTP

# Get usage
cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")

alerts = []

if cpu > CPU_THRESHOLD:
    alerts.append(f"High CPU Usage: {cpu}% (Threshold: {CPU_THRESHOLD}%)")

if memory > MEMORY_THRESHOLD:
    alerts.append(f"High Memory Usage: {memory}% (Threshold: {MEMORY_THRESHOLD}%)")

if alerts:
    subject = "CPU/Memory Alert"
    body = "\n".join(alerts)
    
    msg = MIMEMultipart()
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))
    
    try:
        with smtplib.SMTP(SMTP_SERVER) as server:
            server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
        print("Alert email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

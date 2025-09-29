import ssl
import socket
from datetime import datetime, timedelta

# Configuration
HOSTNAMES = ["example.com", "myapp.com"]
ALERT_DAYS = 30  # Alert if certificate expires in less than 30 days

def check_ssl_expiry(hostname):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, 443), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                cert = ssock.getpeercert()
        expiry = datetime.strptime(cert['notAfter'], "%b %d %H:%M:%S %Y %Z")
        return expiry
    except Exception as e:
        print(f"Error checking {hostname}: {e}")
        return None

for host in HOSTNAMES:
    expiry_date = check_ssl_expiry(host)
    if expiry_date:
        days_left = (expiry_date - datetime.utcnow()).days
        print(f"{host}: SSL expires on {expiry_date} ({days_left} days left)")
        if days_left < ALERT_DAYS:
            print(f"⚠ ALERT: SSL certificate for {host} expires in {days_left} days!")

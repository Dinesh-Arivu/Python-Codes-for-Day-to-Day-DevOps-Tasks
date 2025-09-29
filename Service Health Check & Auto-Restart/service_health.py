import subprocess
from datetime import datetime

SERVICE = "nginx"
LOG_FILE = "/var/log/service_monitor.log"

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

# Check service status
status = subprocess.call(["systemctl", "is-active", "--quiet", SERVICE])

if status != 0:
    log(f"{SERVICE} is down! Attempting restart...")
    restart_status = subprocess.call(["systemctl", "restart", SERVICE])
    
    if restart_status == 0:
        log(f"{SERVICE} restarted successfully.")
    else:
        log(f"Failed to restart {SERVICE}!")
else:
    log(f"{SERVICE} is running normally.")

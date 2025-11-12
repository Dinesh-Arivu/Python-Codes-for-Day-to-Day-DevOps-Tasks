import subprocess
from datetime import datetime

SERVICES = ["nginx", "docker", "jenkins", "apache", "mysql"]  # List of services
LOG_FILE = "/var/log/service_monitor.log"

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

for service in SERVICES:
    # Check if service is active
    status = subprocess.call(["systemctl", "is-active", "--quiet", service])
    
    if status != 0:
        log(f"{service} is down! Attempting restart...")
        # Restart service (requires root)
        restart_status = subprocess.call(["sudo", "systemctl", "restart", service])
        
        if restart_status == 0:
            log(f"{service} restarted successfully.")
        else:
            log(f"Failed to restart {service}!")
    else:
        log(f"{service} is running normally.")

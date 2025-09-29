import subprocess
from datetime import datetime

APP_DIR = "/var/www/myapp"
SERVICE_NAME = "myapp.service"
LOG_FILE = "/var/log/deploy.log"

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

try:
    # Step 1: Pull latest code from Git
    log("Pulling latest code from Git...")
    subprocess.run(["git", "-C", APP_DIR, "pull", "origin", "main"], check=True)
    log("Code pulled successfully.")

    # Step 2: Restart the application service
    log(f"Restarting service {SERVICE_NAME}...")
    subprocess.run(["systemctl", "restart", SERVICE_NAME], check=True)
    log(f"Service {SERVICE_NAME} restarted successfully.")

    log("Deployment completed successfully!")

except subprocess.CalledProcessError as e:
    log(f"Deployment failed: {e}")

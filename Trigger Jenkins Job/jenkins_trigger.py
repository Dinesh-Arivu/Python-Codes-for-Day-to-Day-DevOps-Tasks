import requests
from datetime import datetime

# Jenkins configuration
JENKINS_URL = "http://jenkins.local:8080/job/myjob/build"
USER = "admin"
API_TOKEN = "apitoken"
LOG_FILE = "/var/log/jenkins_trigger.log"

def log(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {message}")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} - {message}\n")

try:
    res = requests.post(JENKINS_URL, auth=(USER, API_TOKEN))
    if res.status_code in [200, 201, 202]:
        log(f"Jenkins job triggered successfully. Status code: {res.status_code}")
    else:
        log(f"Failed to trigger Jenkins job. Status code: {res.status_code}, Response: {res.text}")

except requests.exceptions.RequestException as e:
    log(f"Error triggering Jenkins job: {e}")

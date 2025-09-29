import os
import subprocess
from datetime import datetime

# Backup paths
SRC = "/var/www/html"
DEST = f"/backup/{datetime.now().strftime('%Y-%m-%d')}"
os.makedirs(DEST, exist_ok=True)

# Step 1: Backup files using rsync
subprocess.run(["rsync", "-av", SRC + "/", DEST + "/"])

# Step 2: Backup MySQL database safely
DB_USER = "root"
DB_PASS = "MyPass"  # For security, consider using .my.cnf or environment variable
DB_NAME = "mydb"
DB_BACKUP_FILE = os.path.join(DEST, "mydb.sql")

with open(DB_BACKUP_FILE, "w") as f:
    subprocess.run(
        ["mysqldump", f"-u{DB_USER}", f"-p{DB_PASS}", DB_NAME],
        stdout=f
    )

print(f"Backup completed successfully:\nFiles → {DEST}\nDB → {DB_BACKUP_FILE}")

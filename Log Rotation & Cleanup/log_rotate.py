import os
import time
import gzip
import shutil

LOG_DIR = "/var/log/myapp"
ARCHIVE_DIR = "/var/log/myapp/archive"
LOG_RETENTION_DAYS = 7
ARCHIVE_RETENTION_DAYS = 30
now = time.time()

# Ensure archive directory exists
os.makedirs(ARCHIVE_DIR, exist_ok=True)

# Step 1: Compress and move old logs to archive
for filename in os.listdir(LOG_DIR):
    path = os.path.join(LOG_DIR, filename)
    if os.path.isfile(path) and filename.endswith(".log"):
        file_age = now - os.stat(path).st_mtime
        if file_age > LOG_RETENTION_DAYS * 86400:
            archive_path = os.path.join(ARCHIVE_DIR, filename + ".gz")
            with open(path, 'rb') as f_in:
                with gzip.open(archive_path, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            os.remove(path)
            print(f"Archived {path} → {archive_path}")

# Step 2: Delete archived logs older than ARCHIVE_RETENTION_DAYS
for filename in os.listdir(ARCHIVE_DIR):
    path = os.path.join(ARCHIVE_DIR, filename)
    if os.path.isfile(path) and filename.endswith(".gz"):
        file_age = now - os.stat(path).st_mtime
        if file_age > ARCHIVE_RETENTION_DAYS * 86400:
            os.remove(path)
            print(f"Deleted old archive {path}")

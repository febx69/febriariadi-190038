import os
import time
from datetime import datetime

# Konfigurasi
REPO_PATH = r"D:\Airdrop\febriariadi-190038" # <-- Ganti ke path lokal repo kamu
COMMIT_MESSAGE = "Automated commit"
BRANCH_NAME = "main"  # atau 'master', sesuaikan dengan branch kamu
PUSH_TIMES_PER_DAY = 5
INTERVAL_SECONDS = (24 * 60 * 60) // PUSH_TIMES_PER_DAY  # Biar merata dalam 24 jam

def git_push():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.chdir(REPO_PATH)
    os.system("git add .")
    os.system(f'git commit -m "{COMMIT_MESSAGE} at {now}"')
    os.system(f"git push origin {BRANCH_NAME}")
    print(f"Push dilakukan pada {now}")

def main():
    for _ in range(PUSH_TIMES_PER_DAY):
        git_push()
        print(f"Tunggu {INTERVAL_SECONDS} detik untuk push berikutnya...")
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()

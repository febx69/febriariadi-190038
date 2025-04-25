import os
import time
from datetime import datetime

# Konfigurasi
REPO_PATH = r"D:\Airdrop\febriariadi-190038"  # Ganti path repo kamu
TARGET_FILE = "1.txt"  # Nama file yang mau diedit kecil
COMMIT_MESSAGE = "Automated commit"
BRANCH_NAME = "main"  # Ganti kalau branch kamu bukan 'main'
PUSH_TIMES_PER_DAY = 5
INTERVAL_SECONDS = (60) // PUSH_TIMES_PER_DAY  # Interval 5x sehari

def modify_file():
    """Tambah timestamp baru ke file target supaya ada perubahan."""
    file_path = os.path.join(REPO_PATH, TARGET_FILE)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as f:
        f.write(f"\nUpdate at {now}")

def git_push():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.chdir(REPO_PATH)
    os.system("git add .")
    os.system(f'git commit -m "{COMMIT_MESSAGE} at {now}"')
    os.system(f"git push origin {BRANCH_NAME}")
    print(f"Push berhasil pada {now}")

def main():
    for _ in range(PUSH_TIMES_PER_DAY):
        modify_file()
        git_push()
        print(f"Tunggu {INTERVAL_SECONDS} detik untuk push berikutnya...")
        time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()

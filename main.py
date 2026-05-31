import os
from dataclasses import dataclass 
from pathlib import Path
import shutil
from Checkers.SpamChecker import SpamChecker

mail_box = "inbox"
keywords = ["partner"]

spam = SpamChecker()

@dataclass
class Mail:
    text: str
    sender: str = None

for filename in os.listdir(mail_box):

    if filename.endswith(".txt"):
        mail_path = os.path.join(mail_box, filename)

        try:
            with open(mail_path, "r", encoding="utf-8", errors="ignore") as f:
                mail = Mail(f.read())
                src = Path(f"inbox/{filename}")
                print(filename)
                if spam.spam_checker(mail):
  
                    dst = Path(f"emails_box/spam/{filename}")

                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(src, dst)
                    
        except Exception as e:
            print("Ошибка:", e)




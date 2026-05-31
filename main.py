from Checkers.SpamChecker import SpamChecker
from Checkers.EscalationChecker import EscalationChecker
from Checkers.AutomaticSystemsChecker import AutomaticSystemsChecker

import os
import shutil

from dataclasses import dataclass 
from pathlib import Path

mail_box = "inbox"
keywords = ["partner"]

spam = SpamChecker()
escalation = EscalationChecker()
auto = AutomaticSystemsChecker()

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

                if spam.check(mail):
                    dst = Path(f"emails_box/spam/{filename}")
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(src, dst)
                    
                elif auto.check(mail):
                    dst = Path(f"emails_box/auto_systems/{filename}")
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(src, dst)
                    
                elif escalation.check(mail):
                    dst = Path(f"emails_box/escalation/{filename}")
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(src, dst)
                    
                    
        except Exception as e:
            print("Ошибка:", e)




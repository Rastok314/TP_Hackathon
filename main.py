from Checkers.SpamChecker import SpamChecker
from Checkers.EscalationChecker import EscalationChecker
from Checkers.AutomaticSystemsChecker import AutomaticSystemsChecker
from Checkers.HRChecker import HRChecker
from Checkers.CommunicationChecker import CommunicationChecker

import os
import shutil

from dataclasses import dataclass 
from pathlib import Path

mail_box = "inbox"
keywords = ["partner"]

escalation = EscalationChecker()

spam = SpamChecker()
auto = AutomaticSystemsChecker()
communication = CommunicationChecker()
hr = HRChecker()

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
                    
                    
                if escalation.check(mail):
                    filename = "ESCALATED_" + filename
                    
                    
                if auto.check(mail):
                    dst = Path(f"emails_box/auto_systems/{filename}")
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(src, dst)
                
                elif communication.check(mail):
                    dst = Path(f"emails_box/communication/{filename}")
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(src, dst)
                    
                elif hr.check(mail):
                    dst = Path(f"emails_box/hr/{filename}")
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy(src, dst)
                

                    
                    
        except Exception as e:
            print("Ошибка:", e)




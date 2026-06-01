from Checkers.SpamChecker import SpamChecker
from Checkers.EscalationChecker import EscalationChecker
from Checkers.AutomaticSystemsChecker import AutomaticSystemsChecker
from Checkers.HRChecker import HRChecker
from Checkers.CommunicationChecker import CommunicationChecker
from Checkers.ServiceRequestsChecker import ServiceRequestsChecker
from Checkers.DocumentationChacker import DocumentationChecker

import os
import shutil
import logging

from dataclasses import dataclass 
from pathlib import Path

logging.basicConfig(
    filename="classifier.log",
    level=logging.INFO,
    encoding="utf-8",
    format="%(asctime)s | %(levelname)s | %(message)s"
)

mail_box = "data/inbox"

escalation = EscalationChecker()

spam = SpamChecker()
auto = AutomaticSystemsChecker()
communication = CommunicationChecker()
hr = HRChecker()
service = ServiceRequestsChecker()
docs = DocumentationChecker()

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
                src = Path(f"data/inbox/{filename}")
                
                if spam.check(mail):
                    logging.info(f"{filename} -> spam")
                    
                    dst = Path(f"data/emails_box/spam/{filename}")
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(src, dst)
                    
                    continue
                
                new_filename = filename
                
                if escalation.check(mail):
                    new_filename = "ESCALATED_" + filename
                    logging.warning(f"{filename} marked as escalated")
                    
                category = None

                if auto.check(mail):
                    category = "auto_systems"
                elif communication.check(mail):
                    category = "communication"
                elif hr.check(mail):
                    category = "hr"
                elif service.check(mail):
                    category = "service"
                elif docs.check(mail):
                    category = "documents"
                else:
                    category = "trash"

                dst = Path(f"data/emails_box/{category}/{new_filename}")
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(src, dst)

                logging.info(f"{filename} -> {category}")
                      
        except Exception as e:
            logging.info(f"{new_filename} -> {category}")

    else:
        src = Path(f"data/inbox/{filename}")
        dst = Path(f"data/emails_box/trash/{filename}")
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)



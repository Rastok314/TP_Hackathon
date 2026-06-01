import re
from src.KeyWords.HR_KEYWORDS import key_words

class HRChecker:

    def check(self, mail):
        txt = mail.text.lower()
        score = 0

        for key in key_words:
            if re.search(key, txt):
                score += 1
            
        if score >= 2:
            return True
        else:
            return False
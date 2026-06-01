import re
from src.KeyWords.AUTO_KEYWORDS import key_words

class AutomaticSystemsChecker:

    def check(self, mail):
        txt = mail.text.lower()
        score = 0

        for key in key_words:
            if re.search(key, txt):
                score += 1
            
        if score >= 1:
            return True
        else:
            return False
            
        
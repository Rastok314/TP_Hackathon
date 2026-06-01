import re
from KeyWords.SERVICE_KEYWORDS import key_words1, key_words2, key_words3

class ServiceRequestsChecker:

    def check(self, mail):
        txt = mail.text.lower()
        score = 0

        for key in key_words1:
            if re.search(key, txt):
                score += 1
        
        for key in key_words2:
            if re.search(key, txt):
                score += 1
        
        for key in key_words3:
            if re.search(key, txt):
                score += 2
            
        if score >= 2:
            return True
        else:
            return False
            
        
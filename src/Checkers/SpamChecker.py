import re
from src.KeyWords.SPAM_KEYWORDS import key_words

class SpamChecker:
    
    email = r"(from|от|от кого):.*@(company|corp)\.(ru|com|local)"

    def check(self, mail):
        flag = False
        
        txt = mail.text.lower()
        score = 0
        
        if not re.search(self.email, txt):
            score += 1
            
        for key in key_words:
            if re.search(key, txt):
                score += 1
                flag = True
        
        if "парол" in txt and flag:
            score += 2
            
        if flag and "влож" in txt and score >= 2:
            score += 1
            
        if score >= 3:
            return True
        else:
            return False
            
        
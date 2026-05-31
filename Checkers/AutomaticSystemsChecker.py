import re
class AutomaticSystemsChecker:
    
    key_words = [
        r"сгенерирован",
        r"автомат",
        r"мониторин",
    ]

    def check(self, mail):
        txt = mail.text.lower()
        score = 0

        for key in self.key_words:
            if re.search(key, txt):
                score += 1
            
        if score >= 1:
            return True
        else:
            return False
            
        
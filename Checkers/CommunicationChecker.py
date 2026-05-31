import re
class CommunicationChecker:
    
    key_words = [
        r"созвон",
        r"созвоним",
        r"звон(ок|ок)?",
        r"встреч(а|у|е)?",
        r"meeting",
        r"митинг",
        r"синк",
        r"sync",
        r"обсуд(ить|им)",
        r"давай.*(созвон|встре)",
        r"нужно.*(созвон|обсуд)",
        r"на\s*[2-9]\d*\s*мин"
    ]

    def check(self, mail):
        txt = mail.text.lower()
        score = 0

        for key in self.key_words:
            if re.search(key, txt):
                score += 1
            
        if score >= 2:
            return True
        else:
            return False
            
        
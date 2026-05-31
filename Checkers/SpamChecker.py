import re
class SpamChecker:
    
    key_words = [
        r"вы\s*выиграли",
        r"поздравляем",
        r"перейд(и|ите)\s*по\s*ссылке",
        r"аккаунт.*заблок",
        r"bit\.ly",
        r"победител",
        r"розыгрыш", 
        r"конкурс", 
        r"приз", 
        r"банковск.*", 
        r"немедленно", 
        r"срочно", 
        r"spam",
        r"спам",
        r"заблокир",
        r"акци"
    ]
    
    email = r"(from|от|от кого):.*@(company|corp)\.(ru|com|local)"

    def check(self, mail):
        flag = False
        
        txt = mail.text.lower()
        score = 0
        
        if not re.search(self.email, txt):

            score += 1
            
        for key in self.key_words:
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
            
        
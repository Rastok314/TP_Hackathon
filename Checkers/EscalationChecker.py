import re
class EscalationChecker:
    
    key_words = [
        r"повт|напомин",
        r"(без|нет)\s*ответа.*\d+\s*(дней|дня|часов|недель)",
        r"прошу\s*ускорить|прошу\s*эскалировать",
        r"(втор*|третий*|четверт*|[2-9]).*запрос|письмо|обращение"
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
            
        
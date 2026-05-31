import re
class HRChecker:
    
    key_words = [
        r"human\s*resources",
        r"кадров",
        r"отдел\s*кадров",
        r"персонал",
        r"сотрудник",
        r"работник",
        r"штат",
        r"оформлен",
        r"трудоустрой",
        r"ваканси",
        r"собеседован",
        r"интервью",
        r"кандидат",
        r"резюме",
        r"cv",
        r"hire",
        r"onboard",
        r"онбординг",
        r"отпуск",
        r"больничн",
        r"график",
        r"смен",
        r"выходн",
        r"отгул",
        r"командировк",
        r"зарплат",
        r"оклад",
        r"преми",
        r"бонус",
        r"выплат",
        r"перевод\s*денег",
        r"bank\s*transfer",
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
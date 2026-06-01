from src.Checkers.EscalationChecker import EscalationChecker
from src.main import Mail

def test_escalation_detect():
    mail = Mail(
        text="Это уже третий запрос. Прошу эскалировать."
    )
    assert EscalationChecker().check(mail) is True


def test_escalation_not_detect():
    mail = Mail(
        text="Прошу предоставить доступ к VPN."
    )
    assert EscalationChecker().check(mail) is False
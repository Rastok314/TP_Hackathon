from src.Checkers.AutomaticSystemsChecker import AutomaticSystemsChecker
from src.main import Mail

def test_auto_detect():
    mail = Mail(
        text="Автоматическое уведомление от системы мониторинга."
    )
    assert AutomaticSystemsChecker().check(mail) is True


def test_auto_not_detect():
    mail = Mail(
        text="Коллеги, предлагаю созвон."
    )
    assert AutomaticSystemsChecker().check(mail) is False
from src.Checkers.SpamChecker import SpamChecker
from src.main import Mail

def test_spam_detect():
    mail = Mail(
        text="Поздравляем! Вы выиграли приз. Для верификации перейдите по ссылке."
    )
    assert SpamChecker().check(mail) is True


def test_spam_not_detect():
    mail = Mail(
        text="Не работает Outlook. Прошу помочь."
    )
    assert SpamChecker().check(mail) is False
from src.Checkers.CommunicationChecker import CommunicationChecker
from src.main import Mail

def test_communication_detect():
    mail = Mail(
        text="Предлагаю созвон на 30 минут для обсуждения."
    )
    assert CommunicationChecker().check(mail) is True


def test_communication_not_detect():
    mail = Mail(
        text="Не работает принтер."
    )
    assert CommunicationChecker().check(mail) is False
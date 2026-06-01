from src.Checkers.ServiceRequestsChecker import ServiceRequestsChecker
from src.main import Mail

def test_service_detect():
    mail = Mail(
        text="Не работает Outlook. Нужна помощь."
    )
    assert ServiceRequestsChecker().check(mail) is True


def test_service_not_detect():
    mail = Mail(
        text="Направляю договор на согласование."
    )
    assert ServiceRequestsChecker().check(mail) is False
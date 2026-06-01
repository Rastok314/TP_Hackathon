from src.Checkers.HRChecker import HRChecker
from src.main import Mail

def test_hr_detect():
    mail = Mail(
        text="Направляю больничный лист. Период нетрудоспособности 10 дней."
    )
    assert HRChecker().check(mail) is True


def test_hr_not_detect():
    mail = Mail(
        text="Не работает Slack."
    )
    assert HRChecker().check(mail) is False
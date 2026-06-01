from src.Checkers.DocumentationChacker import DocumentationChecker
from src.main import Mail

def test_docs_detect():
    mail = Mail(
        text="Просим согласовать договор и вернуть с правками."
    )
    assert DocumentationChecker().check(mail) is True


def test_docs_not_detect():
    mail = Mail(
        text="Ноутбук сломался, нужна диагностика."
    )
    assert DocumentationChecker().check(mail) is False
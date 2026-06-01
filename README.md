# TP_Hackathon

Описание проекта

Проект представляет собой систему автоматической классификации входящих email-сообщений.

Каждое письмо анализируется набором правил (checkers) и относится к одной из категорий:
- Spam
- Escalation
- Automatic Systems
- HR
- Communication
- Service Requests
- Documentation
- Trash (по умолчанию)

Как работает система

1. Письма берутся из папки `data/inbox`
2. Каждое письмо анализируется набором чекеров:
   - SpamChecker
   - EscalationChecker
   - AutomaticSystemsChecker
   - HRChecker
   - CommunicationChecker
   - ServiceRequestsChecker
   - DocumentationChecker
3. Определяется категория письма
4. Файл копируется в соответствующую папку `data/emails_box/`
5. При необходимости письмо помечается как `ESCALATED_`
6. Результаты работы логируются

Структура проекта

src/
  - Checkers/              - модули классификации писем
  - KeyWords/              - ключевые слова для анализа
  - main.py                - основной скрипт обработки писем

tests/                   - тесты (pytest)

data/
  - inbox/                 - входящие письма
  - emails_box/            - результат классификации по папкам

run.sh                   - запуск приложения (Linux / WSL)  
run.bat                  - запуск приложения (Windows)   
requirements.txt        - зависимости

Запуск проекта
1. Зайти в корневую папку проекта
2. Запуск main

Linux / WSL / Git Bash

```bash
chmod +x run.sh
./run.sh start
```

Windows

```bat
run.bat start
```

3. Запуск tests

Linux / WSL / Git Bash

```bash
./run.sh test
```
Windows

```bat
run.bat test
```

Логирование

* файл: `classifier.log`
* формат:

```
YYYY-MM-DD HH:MM:SS | LEVEL | MESSAGE
```

Используемые технологии

* Python 3.10+
* pathlib, os, shutil
* logging
* pytest (для тестов)

This is a student project for the final module of ["Test automation with Python and Selenium" Course](https://stepik.org/course/575).
For English description please scroll down.

# Комментарии к ревью финального проекта
Структура проекта несколько отличается от предложенной преподавателями курса. Это сделано не по глупости, а намеренно.
- Тесты выделены в модуль tests. С ростом числа файлов с тестами, а также вспомогательных файлов типа настроек и линтера, куча в корне выглядит неопрятно, поэтому тесты были вынесены. Это заодно позволило меньше париться с импортами в тестах.
- В корне отсутствует `__init__.py`, так как он тоже создавал проблемы с импортами. Просьба не снижать баллы из-за этого. Зато он есть в папке tests, откуда тесты могу импортироваться куда-то ещё)
- В проекте используется линтер [flake8](https://flake8.pycqa.org/en/latest/) и завязанный на него [pre-commit-hook](https://pre-commit.com/). Это не позволяет закоммитить в репозиторий код, не соответствующий PEP8. Их конфигурации соответствуют файлы `.flake8` и `.pre-commit-config.yaml` соответственно.
- В репозитории используется статический анализатор кода [deepsource](https://deepsource.com/), несколько более строгий, чем flake8. Анализирует pull-requests на github, позволяя следить за качеством кода. За его конфигурацию отвечает `.deepsource.toml`

В requirements.txt находится больше 2 пакетов, так как это делалось через `pip freeze > requirements.txt` после установки pytest, selenuim и pre-commit на чистое окружение, что гарантирует соответствие версий всех пакетов тем, что загрузились у меня.

## Установка/Installation
Предполагается что у вас уже установлен chromedriver.

It is assumed that chromedriver is already installed on your computer.

Mac/Linux

```shell
python -m venv env
source env/bin/activate
pip install -r requirements.txt

```

Windows:

```commandline
py -m venv env
.\env\Scripts\activate
py -m pip install -r requirements.txt

```
Не могу проверить работает ли под Windows, но вроде бы так должно быть

Can't check whether it works on Windows, but it must be so 

## Запуск/Running

```commandline
pytest -v --tb=line --language=en -m need_review
```
Но можно и без параметров, просто `pytest`.

# Description

This is a student project for Selenium practice.

Site under test - http://selenium1py.pythonanywhere.com/

The stack is Python, Pytest, and Selenium. Plus some additional libs like allure that were not taught on the course.

In addition to the course stack I also use [flake8](https://flake8.pycqa.org/en/latest/) linter as [pre-commit hook](https://pre-commit.com/), that are configured in `.flake8` and `.pre-commit-config.yaml` respectively.

This GitHub repo is equipped with [deepsource](https://deepsource.com/) static code analyzer, which is configured in `.deepsource.toml`
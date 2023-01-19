# selenium_rt_tests

Итоговое задание по курсу SkillFactory "Тестировщик-автоматизатор на Python".

Тестируемый проект расположен по адресу https://b2c.passport.rt.ru.

Для клонирования проекта следует выполнить команду:
git clone https://github.com/pvl1524/selenium_rt_tests.git

В каталоге /pages расположены файлы
- base_page.py, который содержит описание базового класса BasePage;
- auth_page.py, который содержит описание класса AuthPage страницы авторизации;
- locators.py, который содержит локаторы страницы авторизации; 

В каталоге /tests располагается файл test_rt_auth.py с позитивными и негативными тестами формы авторизации личного кабинета Ростелеком.

Для установки необходимых библиотек в корневом каталоге проекта следует выполнить следующие команды:
pip install pytest
pip install pytest-selenium
pip install pytest-check
pip install 2captcha-python

При выполнении задания используется Selenium четвертой версии. 

Для запуска тестов следует использовать Crhomedriver, который можно найти по адресу https://chromedriver.chromium.org/downloads 
Предполагается, что файл cromedriver находиться в корневом каталоге проекта.

Для запуска тестов в корневом каталоге проекта следует выполнить команду
python -m pytest -v --driver Chrome --driver-path chromedriver tests/test_rt_auth.py

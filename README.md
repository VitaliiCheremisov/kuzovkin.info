# kuzovkin.info
Проект парсер данных. Сбор задач ЕГЭ по информатике с url
https://kpolyakov.spb.ru/school/ege/generate.htm

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/VitaliiCheremisov/foodgram-project-react.git
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
* Если у вас Linux/macOS
    ```
    source env/bin/activate
    ```
* Если у вас windows
    ```
    source env/scripts/activate
    ```
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить выполнение файла main.py


## Что необходимо.
- Обязательно установить chromedriver для Google Chrome браузера, необходим для работы 
  библиотеки selenium. Для этого необходимо установить на локальном компьютере версию chromedriver,
  совместимую с версией браузера.
- В строке 14 файла main.py указать путь с chromedriver на вашем локальном компьютере.
- Иметь стабильное интернет-соединение.

## Что реализовано.
С учетом структуры сайта парсер работает по следующей логике:
- Собираются данные о темах из выпадающего списка генератор задач.
- Формируются ссылки для каждой отдельной подтемы с задачами.
- После предпросмотра ссылки - собираются данные.
- Записываются в Excel-файл.
  
Технологии
```
Python 3.10
beautifulsoup4==4.12.3
openpyxl==3.1.5
selenium==4.23.1
webdriver-manager==4.0.2
lxml==5.3.0
numpy==2.1.0
pandas==2.2.2
```

Автор
- [Виталий Черемисов](https://github.com/VitaliiCheremisov)

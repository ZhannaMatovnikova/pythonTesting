Запуск автотеста с использваонием PyCharm, playwright - добавление объявления в избранное(сайт avito)

Требования:
OS Windows 11 Домашняя для одного языка

Процессор	AMD Ryzen 7 5825U with Radeon Graphics            2.00 GHz
Оперативная память	16,0 ГБ 
Тип системы	64-разрядная операционная система, процессор x64

Предусловия
1. Установлен PyCharm последней версии
2. Установлен Python последней версии
3. Открыт новый проект PyCharm

Запуск теста:

Настройка окружения, подготовка файлов
1. В терминале ввести venv\Scripts\activate
2. Сохранить файлы .gitignore, conftest.py, README.MD, requitements.txt  директории проекта
3. Папки .idea, config,fixtures, pages, tests разместить в директории проекта. Папка venv должна появиться при запуске нового проекты, также должна быть папка .pytest_cache - проверить после выполнения п.8
4. В терминал ввести pip3 install pytest, запустить Enter
5. Убедиться, что версия pytest соответствует версии в файле requirements.txt, изменить при необходимости pytest == ...

Настройка требований
6. В терминал ввести pip3 install -r requirements.txt , запустить Enter
7. upgrade pip при необходимости, следуя подсказкам терминала

Установка playwright
8. В терминал ввести playwright install, запустить Enter
Тест
9. После проверки всех файлов на наличие ошибок и неточностей, В терминал ввести pytest . , запустить Enter


Ожидаемый результат: откроется страница с объявлением, объявление будет добавлено в "Избранное", терминал выдаст инфо зеленым цветом "1 passed"
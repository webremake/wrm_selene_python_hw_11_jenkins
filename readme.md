**Набор команд для работы из командной строки**

`pytest --alluredir=tests/allure-results`

или
`pytest`

если `--alluredir=tests/allure-results` вынесено в `pytest.ini` 


`allure generate tests/allure-results --clean -o tests/allure-report`

`allure open tests/allure-report`

можно еще так

`pytest --alluredir=tests/allure-results`

`allure serve tests\allure-results`

но тогда папка  `allure-report` генерится в
`C:\Users\Heorhi\AppData\Local\Temp\19817269894530779\allure-report`
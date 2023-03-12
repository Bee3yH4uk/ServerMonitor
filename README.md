# ServerMonitor

Данная программа предназначена для проверки работоспособности указанных хостов и портов.

Для работы программы требуется установить следующие зависимости:
- Python 3.7 или выше
- Установить зависимости
```shell
pip install -r requirements.txt
```

## Запуск

Программу можно запустить либо с помощью файла start.py, либо через командную строку.

### Запуск через файл start.py

```
python start.py
```

### Запуск через командную строку
#### Аргументы:
- --path (-p) - путь к csv файлу
- --ignore_errors (-i) - игнорирование ошибок при запуске. Допустимые значения: T - игнорировать, F - не игнорировать


```
python start.py --path <path_to_csv_file> --ignore_errors <T/F>
```

Пример:
```
python start.py --path data.csv --ignore_errors T
```

### Запуск на UNIX системах

```
python3 start.py --path <path_to_csv_file> --ignore_errors <T/F>
```

# Wildberries Телеграм бот


**Не забудьте дать права пользователю на проект:**

``` bash
sudo chown -R [user]:[user] ./
```

#### Документация по проекту **wb_parser** - <a href="https://telegra.ph/Parsing-Wildberries-11-05">ТУТ</a>

<br>

### Установка:

1. В файле с переменными окружения `.env` прописать значения:

    - `TOKEN_BOT` - Токен телеграм бота
    - `DOMAIN` - Домен или Хост сервера с API(Проект wb_parser)
    - `PAGE_SIZE` - Кол-во товаров на странице (кол-во товаро в сообщение)

### Запуск:

1. Установить виртуальное окружение и активировать его:
``` bash
python -m venv venv
source venv/bin/activate
```

2. Установка зависимостей
``` bash
pip install -r requirements.txt
```

3. Запуск бота
``` bash
python main.py
```

### Запуск (Docker):

1. Билд докер-контейнеров:
``` bash
./scripts/build.sh
```

2. Поднять в продакшн
``` bash
./scripts/up_prod.sh
```

3. Поднять локально
``` bash
./scripts/up_local.sh
```

4. Остановить проект в продакшн
``` bash
./scripts/kill_prod.sh
```



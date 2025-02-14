# UTF_test_task

## Добрый день, проект готов.
Предложил на выбор два подхода: 
- через кастомные менеджеры
- через логику выбора во вьюшке

## Стек: 
Python, Django\DRF, DjangoORM, sqlite

## Установка:
```bash
git clone https://github.com/Richman-24/UTF_test_task.git

python3 venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## Запуск:
- создать файл .env в корне проекта, заполнить по примеру из .env.example
- применить миграции

```bash
python3 manage.py migrate
python3 manage.py collectstatic # Для адекватного отображения авто-документации
```

## Эндпоинты
GET 127.0.0.1:8000/api/v1/foods/: Получить список категорий с опубликованными в них объектами.

Пример ответа:
```json
[
    {
        "id": 1,
        "name_ru": "Кофе",
        "name_en": null,
        "name_ch": null,
        "order_id": 10,
        "foods": [
            {
                "internal_code": 321,
                "code": 123,
                "name_ru": "Americano",
                "description_ru": "Кофе чёрный",
                "description_en": null,
                "description_ch": null,
                "is_vegan": true,
                "is_special": false,
                "cost": "200.00",
                "additional": []
            }
        ]
    },
    {
        "id": 2,
        "name_ru": "Булка",
        "name_en": null,
        "name_ch": null,
        "order_id": 20,
        "foods": []
    },
]
```
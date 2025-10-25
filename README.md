# Scooter Rent API Autotest

Автоматизированный тест для проверки создания заказа и получения информации о заказе по трек-номеру.

## Структура проекта

- `configuration.py` - настройки приложения
- `data.py` - тестовые данные
- `sender_stand_request.py` - методы API
- `test_scooter_api.py` - основной тест
- `README.md` - документация
- `.gitignore` - упрощенный гитигнор

## Описание теста

`test_create_order_and_get_by_track` - проверяет полный цикл работы с заказом:

1. Создание заказа через POST `/api/v1/orders`
2. Извлечение трек-номера из ответа
3. Получение заказа через GET `/api/v1/orders/track`
4. Проверка кодов ответа (201 при создании, 200 при получении)

## Запуск тестов

```bash
# Установите зависимости
pip install requests

# Запустите тест
python test_scooter_api.py

# Или через pytest
python -m pytest test_scooter_api.py -v

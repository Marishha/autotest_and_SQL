import requests


class ScooterAPITest:
    # Конфигурация
    BASE_URL = "https://f250cabb-5ee2-4286-9442-4a5c5c98a6c1.serverhub.praktikum-services.ru"
    
    # Тестовые данные для создания заказа
    ORDER_DATA = {
        "firstName": "Naruto",
        "lastName": "Uzumaki", 
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2024-10-25",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }
    
    @staticmethod
    def create_order(order_data):
        """Создание нового заказа"""
        url = ScooterAPITest.BASE_URL + "/api/v1/orders"
        response = requests.post(url, json=order_data)
        return response
    
    @staticmethod
    def get_order_by_track(track_number):
        """Получение заказа по номеру трека"""
        url = ScooterAPITest.BASE_URL + "/api/v1/orders/track"
        params = {"t": track_number}
        response = requests.get(url, params=params)
        return response
    
    @staticmethod
    def test_create_and_get_order():
        """Основной тест: создание заказа и получение по треку"""
        print("=== Тест: Создание заказа и получение по треку ===\n")
        
        # 1. Выполнить запрос на создание заказа
        print("1. Создаем заказ...")
        create_response = ScooterAPITest.create_order(ScooterAPITest.ORDER_DATA)
        
        # Проверяем, что заказ создан успешно
        assert create_response.status_code == 201, f"Ошибка создания заказа: {create_response.text}"
        print(f"   ✓ Заказ создан успешно, статус: {create_response.status_code}")
        
        # 2. Сохранить номер трека заказа
        response_data = create_response.json()
        track_number = response_data.get("track")
        assert track_number is not None, "Трек номер не получен в ответе"
        print(f"   ✓ Трек номер заказа: {track_number}")
        
        # 3. Выполнить запрос на получение заказа по треку
        print(f"2. Получаем заказ по треку {track_number}...")
        get_response = ScooterAPITest.get_order_by_track(track_number)
        
        # 4. Проверить, что код ответа равен 200
        assert get_response.status_code == 200, f"Ошибка получения заказа: {get_response.text}"
        print(f"   ✓ Заказ получен успешно, статус: {get_response.status_code}")
        
        # Дополнительная проверка - данные заказа соответствуют отправленным
        order_info = get_response.json()
        order_data_response = order_info.get("order", {})
        
        print(f"3. Проверяем данные заказа:")
        print(f"   - ID заказа: {order_data_response.get('id')}")
        print(f"   - Имя: {order_data_response.get('firstName')}")
        print(f"   - Фамилия: {order_data_response.get('lastName')}")
        print(f"   - Адрес: {order_data_response.get('address')}")
        print(f"   - Статус: {order_data_response.get('status')}")
        print(f"   - Трек: {order_data_response.get('track')}")
        
        # Проверяем, что трек в ответе совпадает с запрошенным
        assert order_data_response.get('track') == track_number, "Трек номер в ответе не совпадает"
        
        print("\n✅ Тест пройден успешно! Заказ создан и получен по треку.")
        return True


# Дополнительные утилиты для работы с БД
class DatabaseUtils:
    @staticmethod
    def get_db_connection_command():
        """Команда для подключения к базе данных"""
        return "psql -U morty -d scooter_rent"
    
    @staticmethod
    def get_db_password():
        """Пароль для базы данных"""
        return "smith"


if __name__ == "__main__":
    # Запуск теста
    try:
        ScooterAPITest.test_create_and_get_order()
    except Exception as e:
        print(f"\n❌ Тест не пройден: {e}")
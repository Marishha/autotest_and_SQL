import sender_stand_request
import data


def test_create_order_and_get_by_track():
    """
    Тест проверяет, что можно создать заказ и получить его по трек-номеру
    """
    # Создаем заказ
    create_response = sender_stand_request.SenderStandRequest.create_order(
        data.OrderData.get_create_order_data()
    )
    
    # Проверяем, что заказ создан успешно
    assert create_response.status_code == 201
    
    # Получаем трек-номер
    track_number = create_response.json().get("track")
    assert track_number is not None
    
    # Получаем заказ по трек-номеру
    get_response = sender_stand_request.SenderStandRequest.get_order_by_track(track_number)
    
    # Проверяем, что заказ найден
    assert get_response.status_code == 200


if __name__ == "__main__":
    test_create_order_and_get_by_track()

import requests
from configuration import Configuration


class SenderStandRequest:
    @staticmethod
    def create_order(order_data):
        url = Configuration.BASE_URL + Configuration.CREATE_ORDER_PATH
        return requests.post(url, json=order_data)
    
    @staticmethod
    def get_order_by_track(track_number):
        url = Configuration.BASE_URL + Configuration.GET_ORDER_BY_TRACK_PATH
        params = {"t": track_number}
        return requests.get(url, params=params)
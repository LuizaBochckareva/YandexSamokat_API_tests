import configuration
import requests
import data


# создание нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body)


order_track = post_new_order(data.order_body).json()["track"]
print(order_track)


# получение данных о заказе по треку api/v1/orders/track?t=123456
def get_info_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDER_BY_TRACK + str(track))


response = get_info_order(order_track)
print(response.status_code)
print(response.json())

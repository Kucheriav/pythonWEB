import requests

request_object =  ['Барнаул', 'Мелеуз', 'Йошкар-Ола']
for object in request_object:
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={object}&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        if json_response["response"]["GeoObjectCollection"]["featureMember"]:
            toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
            print(toponym['name'], 'принадлежит к ', toponym['metaDataProperty']['GeocoderMetaData']['Address']['Components'][2]['name'])
        else:
            print('Ничего не нашлось')
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")


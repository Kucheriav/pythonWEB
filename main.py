import requests


class CoordByNameException(Exception):
    pass


def coor_by_name(name):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={name}&format=json"
    response = requests.get(geocoder_request)
    if response:
        json_response = response.json()
        if toponym := json_response["response"]["GeoObjectCollection"]["featureMember"]:
            return toponym[0]["GeoObject"]['Point']['pos'].replace(' ',',')
        else:
            raise CoordByNameException('Ничего не нашлось')
    else:
        raise CoordByNameException("Ошибка выполнения запроса:")


def y_coord(target):
    try:
        y = coor_by_name(target).split(',')[1]
    except Exception as e:
        print(f'При обработке города {target} произошла ошибка: {e}')
    else:
        return y


cities = list()
print('Здраствуйте! Введите претендентов на соискание звания "Самый Южный Город"!')
print('Введите пустую строку для окончания ввода')
while city := input():
    y = y_coord(city)
    if isinstance(y, str):
        cities.append([city, y])

if cities:
    cities.sort(key=lambda x: x[1])
    print(f'И в номинации "Самый Южный Город" побеждает {cities[0][0].capitalize()}!')
else:
    print('Вы ничего не ввели')
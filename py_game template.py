import os
import sys

import pygame
import requests


def reverse_weird_yandex_coordinates(coord):
    x, y = coord.split(',')
    return y + ',' + x


def get_a_picture(coords):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={coords}&spn=0.1,0.1&l=map"
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)
    return map_file

slides_list = list()
coords_list = [reverse_weird_yandex_coordinates(x) for x in ('59.894694,30.653147', '59.894694,30.653147', '55.206981,34.291738')]
for el in coords_list:
    slides_list.append(get_a_picture(el))

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.

screen.blit(pygame.image.load(slides_list[2]), (0, 0))
# Переключаем экран и ждем закрытия окна.
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

# Удаляем за собой файл с изображением.
os.remove(map_file)
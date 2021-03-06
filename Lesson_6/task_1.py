# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение
# светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

import time


class TrafficLight(object):
    _colors = {'Красный': 7, 'Желтый': 2, 'Зеленый': 5}

    def __init__(self):
        self._color = self._colors['Красный']

    def running(self):
        for cl, tm in self._colors.items():
            self._color = cl
            print(self._color)
            # print(f'{self._color} {tm}сек.')
            time.sleep(tm)

    def get_sate(self):
        return self._color


trafic_lighter = TrafficLight()
trafic_lighter.running()
print('Программа завершила работу')

# 1. Создать класс TrafficLight (светофор).
# определить у него один атрибут color (цвет) и метод running (запуск);
# атрибут реализовать как приватный;
# в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) —
# на ваше усмотрение;
# переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
# проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и
# завершать скрипт.

# Саша, не совсем понял зачем проверять порядок режимов раз мы сами их меняем по кругу приватными методами.
# Потом кажется понял, но не понял как проверять без большого объема кода.
# Прикладываю 2 варианта решения, потому что иметь отдельный метод для переключения цвета кажется логичным,
# а в задании речь только о запуске.
# max_count просто чтобы не зацикливать бесконечно(хоть светофоры так и работают)

# import time
# from itertools import cycle
#
#
# class TrafficLight:
#
#     __color = ('red', 'yellow', 'green')
#
#     def running(self, max_count):
#         traffic_iter = cycle(self.__color)
#         for i in range(max_count):
#             print('\033[31m{}\033[0m'.format(next(traffic_iter)))
#             time.sleep(7)
#             print('\033[33m{}\033[0m'.format(next(traffic_iter)))
#             time.sleep(2)
#             print('\033[32m{}\033[0m'.format(next(traffic_iter)))
#             time.sleep(5)
#
#     def running_2(self, max_count):
#         traffic_iter = cycle(self.__color)
#         for i in range(max_count):
#             self.__next_color(traffic_iter, '\033[31m{}\033[0m', 7)
#             self.__next_color(traffic_iter, '\033[33m{}\033[0m', 2)
#             self.__next_color(traffic_iter, '\033[32m{}\033[0m', 5)
#
#     @staticmethod
#     def __next_color(traffic_iter, color, sleep):
#         print(color.format(next(traffic_iter)))
#         time.sleep(sleep)
#
#
# traffic_light = TrafficLight()
# traffic_light.running(10)
# traffic_light.running_2(10)


# 2. Реализовать класс Road (дорога).
# определить атрибуты: length (длина), width (ширина);
# значения атрибутов должны передаваться при создании экземпляра класса;
# атрибуты сделать защищёнными;
# определить метод расчёта массы асфальта, необходимого для покрытия всей дороги;
# использовать формулу: длина*ширина*масса асфальта для покрытия одного кв. метра дороги асфальтом,
# толщиной в 1 см*число см толщины полотна;
# проверить работу метода.
# Например: 20 м*5000 м*25 кг*5 см = 12500 т.

# class Road:
#
#     def __init__(self, length, width):
#         self._length = length
#         self._width = width
#
#     def calc_weight(self, calc_mass, calc_thickness):
#         return self._length * self._width * calc_mass * calc_thickness
#
#
# new_road = Road(5000, 20)
# mass = int(input('Введите массу асфальта для покрытия одного кв. метра: '))
# thickness = int(input('Введите толщину покрытия в см: '))
# print(f'Для покрытия дороги асфальтом толщиной {thickness} см и массой {mass} кг потребуется '
#       f'{new_road.calc_weight(mass, thickness) / 1000} тонн асфальта')

# 3. Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например,
# {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии
# (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения
# атрибутов, вызвать методы экземпляров.

# class Worker:
#
#     def __init__(self, name, surname, position, wage, bonus):
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = {"wage": wage, "bonus": bonus}


# class Position(Worker):
#
#     @property
#     def get_full_name(self):
#         return f'{self.name} {self.surname}'
#
#     @property
#     def get_total_income(self):
#         return self._income['wage'] + self._income['bonus']
#
#
# worker_1 = Position('Вася', 'Пупкин', 'Пожарный', 50000, 15000)
# print(worker_1.get_full_name)
# print(worker_1.get_total_income)


# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы, и покажите результат.

class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self, direction):
        print(f'Машина {self.name} повернула в{direction}')

    def show_speed(self):
        print(f'Машина {self.name} едет со скоростью {self.speed}')


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Превышение скорости!')


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=False)


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Превышение скорости!')


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town_car_1 = TownCar(60, 'white', 'Hyundai', False)
town_car_1.go()
town_car_1.turn('лево')
town_car_1.show_speed()
town_car_1.stop()

work_car_1 = WorkCar(60, 'yellow', 'Daewoo', False)
work_car_1.go()
work_car_1.turn('право')
work_car_1.show_speed()
work_car_1.stop()

sport_car_1 = SportCar(120, 'pink', 'Ferrari')
sport_car_1.go()
sport_car_1.turn('лево')
sport_car_1.show_speed()
sport_car_1.stop()

police_car_1 = PoliceCar(60, 'black', 'Jeep')
police_car_1.go()
police_car_1.turn('право')
police_car_1.show_speed()
police_car_1.stop()

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw.
# Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.


class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Handle(Stationery):

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


pen = Pen('ручка')
pencil = Pencil('карандаш')
handle = Handle('маркер')

pen.draw()
pencil.draw()
handle.draw()

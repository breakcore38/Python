# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.

class Date:
    date = ''

    def __init__(self, date):
        Date.date = date
        print(date)

    @classmethod
    def extraction(cls):
        try:
            cls.d, cls.m, cls.y = map(int, cls.date.split('.'))
        except ValueError as ex:
            print(f'Error! {ex}')
            return None, None, None
        else:
            return cls.d, cls.m, cls.y

    @staticmethod
    def validate(d, m, y):
        if d is None:
            return None
        try:
            if d not in range(1, 32):
                raise ValueError('День указан некорректно')
            if m not in range(1, 13):
                raise ValueError('Месяц указан некорректно')
            if y < 0:
                raise ValueError('Год указан некорректно')
        except ValueError as err:
            print(f'Ошибка! {err}')
        else:
            return True


date_1 = Date('13.08.1922')
day, month, year = date_1.extraction()
if Date.validate(day, month, year):
    print(f'day = {day} month = {month} year = {year}')
else:
    print('Невалидные данные!')


# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class MyZeroDivisionError(Exception):
    def __str__(self):
        return f'Ошибка! Деление на ноль!'


try:
    arg_1, arg_2 = map(float, input('Введите делимое и делитель через пробел: ').split())
    if arg_2 == 0:
        raise MyZeroDivisionError
except MyZeroDivisionError as ex:
    print(ex)
except ValueError as ex:
    print(f'Ошибка! Введите 2 числа!')
else:
    print(arg_1/arg_2)


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит
# работу скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами
# выводится на экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки.
# Во время ввода пользователем очередного элемента необходимо реализовать проверку типа элемента.
# Вносить его в список, только если введено число. Класс-исключение должен не позволить пользователю
# ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.

class MyEx(Exception):
    def __str__(self):
        return f'Ошибка! Вы ввели не число!'


my_list = []
print('Вводите числа по одному. Для окончания введите "stop": ')

while True:
    try:
        next_arg = input()
        if next_arg.isdigit():
            my_list.append(int(next_arg))
        elif next_arg == 'stop':
            break
        else:
            raise MyEx
    except MyEx as ex:
        print(ex)
print(f'Вы ввели список: {my_list}')


# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.
# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и
# передачу в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру (например, словарь).
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.

def validate(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ValueError:
            print('Недостаточно техники на складе!')
        except KeyError:
            print('Нет такого типа техники на складе!')
    return wrapper


class Storage:
    equipment_units = {}

    @classmethod
    @validate
    def storage_to(cls, unit_type, unit_name, unit_model, unit_count):
        cls.equipment_units[unit_type][unit_name][unit_model]['count'] += unit_count

    @classmethod
    @validate
    def storage_from(cls, unit_type, unit_name, unit_model, unit_count):
        current_count = cls.equipment_units[unit_type][unit_name][unit_model]['count']
        if current_count < unit_count:
            raise ValueError
        else:
            cls.equipment_units[unit_type][unit_name][unit_model]['count'] -= unit_count

    @staticmethod
    def get_all_equipment():
        print(Storage.equipment_units)
        for key, value in Storage.equipment_units.items():
            print(key, value)


class Equipment:
    def __init__(self, name, model, eq_type, count=0):
        self.name = name
        self.model = model
        self.eq_type = eq_type
        try:
            if type(count) is not int:
                self.__count = 0
                raise ValueError
        except ValueError:
            print('Неверный формат входных данных')
        else:
            self.__count = count
        finally:
            self.update_storage_info()

    def update_storage_info(self):
        equipment_storage_info = Storage.equipment_units.get(self.eq_type, {})
        if self.name in equipment_storage_info.keys():
            equipment_storage_info_by_name = equipment_storage_info[self.name]
            if self.model in equipment_storage_info_by_name.keys():
                equipment_storage_info_by_model = equipment_storage_info_by_name[self.model]
                equipment_storage_info_by_model['count'] += self.__count
            else:
                equipment_storage_info_by_name[self.name] = {self.model: {'count': self.__count}}
        else:
            equipment_storage_info[self.name] = {self.model: {'count': self.__count}}

        Storage.equipment_units[self.eq_type] = equipment_storage_info


class Printer(Equipment):
    def __init__(self, name, model, count, colors):
        super().__init__(name, model, 'Printer', count)
        self.colors = colors


class Notebook(Equipment):
    def __init__(self, name, model, count, ram, system_type):
        super().__init__(name, model, 'Notebook', count)
        self.ram = ram
        self.system_type = system_type


printer_1 = Printer('HP', 'XS5850', 2000, ['red', 'blue', 'green'])
printer_2 = Printer('Canon', 'TS304', 500, ['black'])
printer_3 = Printer('Xerox', 'B210', 1700, ['red', 'blue', 'green'])
printer_4 = Printer('Xerox', 'B210', 1300, ['red', 'blue', 'green'])
printer_5 = Printer('Xerox', 'B211', 200, ['red', 'blue', 'green'])

notebook_1 = Notebook('Lenovo', 'ThinkPad X1', 2300, 8, 'Windows')
notebook_2 = Notebook('Mac', 'MacBookAir', 3200, 8, 'MacOS')

Storage.get_all_equipment()

Storage.storage_to(unit_type='Printer', unit_name='Hp', unit_model='XS5050', unit_count=100)
Storage.get_all_equipment()
Storage.storage_to(unit_type='Notebook', unit_name='Lenovo', unit_model='ThinkPad X1', unit_count=100)
Storage.get_all_equipment()


# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, a, b):
        self.complex = (a, b)

    def __str__(self):
        if self.complex[1] == 1:
            return f'{self.complex[0]} + i'
        elif self.complex[1] == -1:
            return f'{self.complex[0]} - i'
        else:
            return f'{self.complex[0]} + {self.complex[1]}i'

    def __add__(self, other):
        return Complex(self.complex[0] + other.complex[0], self.complex[1] + other.complex[1])

    def __mul__(self, other):
        return Complex(self.complex[0] * other.complex[0] - self.complex[1] * other.complex[1],
                       self.complex[0] * other.complex[1] + self.complex[1] * other.complex[0])


complex_1 = Complex(2, 3)
print(f'complex_1 = {complex_1}')
complex_2 = Complex(-1, 1)
print(f'complex_1 = {complex_2}')

complex_3 = complex_1 + complex_2
print(f'complex_3 = {complex_3}')

complex_4 = complex_1 * complex_2
print(f'complex_4 = {complex_4}')

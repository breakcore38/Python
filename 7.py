# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# [[31, 32],    [[3, 5, 32],        [[3, 5, 8, 3],
#  [37, 43],     [2, 4, 6],          [8, 3, 7, 1]]
#  [51, 86]]     [-1, 64, -8]]

# [[31, 32], [37, 43], [51, 86]]      [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]     [[3, 5, 8, 3], [8, 3, 7, 1]]

# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        temp_matrix = []
        try:
            temp_matrix.append([int(el) for el in matrix[0]])
            for i in range(1, len(matrix)):
                if len(matrix[i]) != len(matrix[i-1]):
                    print(f'Exception! Different number of elements in matrix {matrix}')
                    temp_matrix = None
                    break
                else:
                    temp_matrix.append([int(el) for el in matrix[i]])
            self.matrix = temp_matrix
        except ValueError:
            print(f'Exception! ValueError in {matrix}')
            self.matrix = None

    def __str__(self):
        if self.matrix is None:
            return 'None'
        result_str = ''
        for row_str in self.matrix:
            for el_str in row_str:
                result_str += f'{el_str} '
            result_str += '\n'
        return result_str

    def __add__(self, other):
        if self.matrix is None or other.matrix is None:
            print('Addition error! Matrix is None')
            return None
        else:
            # Сложение матриц допускается только для матриц одинакового размера
            if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
                print(f'Impossible to add matrices {self.matrix} and {other.matrix}! Different sizes.')
                return None
            result_matrix = []
            for row_1, row_2 in zip(self.matrix, other.matrix):
                result_row = []
                for el_1, el_2 in zip(row_1, row_2):
                    result_row.append(el_1 + el_2)
                result_matrix.append(result_row)
            return Matrix(result_matrix)


matrix_1 = Matrix([[31, 32], [37, 41], [51, 84]])
print(f'Matrix 1:\n{matrix_1}')

matrix_2 = Matrix([[1, 15], [7, -13], [5, 8]])
print(f'Matrix 2:\n{matrix_2}')

matrix_1_2 = matrix_1 + matrix_2
if matrix_1_2 is not None:
    print(f'Matrix 1 + Matrix 2:\n{matrix_1_2}')

matrix_3 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
print(f'Matrix 3:\n{matrix_3}')

matrix_1_3 = matrix_1 + matrix_3
if matrix_1_3:

    print(f'Matrix 1 + Matrix 3:\n{matrix_1_3}')
#
matrix_4 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
print(f'Matrix 4:\n{matrix_4}')

# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
# абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod
# Саша, я посмотрел разбор ДЗ, но конкретно здесь почему бы не сделать consumption атрибутом класса и
# просто перегрузить конструктор чтобы сразу в нем считать расход ткани?


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def consumption(self):
        return self.param / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, param):
        super().__init__(param)

    @property
    def consumption(self):
        return 2 * self.param + 0.3


coat_1 = Coat(48)
print(f'Fabric consumption for coat = {coat_1.consumption}')
costume_1 = Costume(1.78)
print(f'Fabric consumption for costume = {costume_1.consumption}')

print(f'Total fabric consumption = {coat_1.consumption + costume_1.consumption}')

# 3. Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов:
# сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
# Данные методы должны применяться # только к клеткам и выполнять увеличение, уменьшение, умножение и целочисленное
# (с округлением до целого) деление клеток, соответственно.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
# ячеек этих двух клеток.
# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
# вернёт строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
# вернёт строку: *****\n*****\n*****.


class Cell:
    def __init__(self, num):
        try:
            if num <= 0:
                raise ValueError('num < 0')
            self.num = num
        except TypeError:
            self.num = 1
            print('check num value')
        except ValueError:
            self.num = 1
            print('check num value')

    def __add__(self, other):
        return Cell(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num > 0:
            return Cell(self.num - other.num)
        else:
            print('Subtraction is impossible')

    def __mul__(self, other):
        return Cell(self.num * other.num)

    def __truediv__(self, other):
        return Cell(self.num // other.num)

    def make_order(self, param):
        return (('*' * param) + '\n') * (self.num // param) + '*' * (self.num % param)


cell_1 = Cell(12)
cell_2 = Cell(15)
print(f'{cell_1.make_order(3)}\n')
print(f'{cell_2.make_order(7)}\n')

cell_3 = cell_2 + cell_1
print(cell_3.make_order(8))

cell_4 = cell_2 - cell_1
print(cell_4.make_order(8))

cell_5 = cell_2 * cell_1
print(cell_5.make_order(8))

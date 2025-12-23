import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = np.array(data)
        if self.data.ndim != 2:
            raise ValueError("Матрица должна быть двумерной")

    @property
    def shape(self):
        return self.data.shape

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Операнд должен быть объектом класса Matrix")

        if self.shape != other.shape:
            raise ValueError(
                f"Невозможно сложить матрицы с размерностями {self.shape} и {other.shape}"
            )

        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Операнд должен быть объектом класса Matrix")

        if self.shape != other.shape:
            raise ValueError(
                f"Невозможно выполнить покомпонентное умножение матриц с размерностями {self.shape} и {other.shape}"
            )

        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Операнд должен быть объектом класса Matrix")

        if self.shape[1] != other.shape[0]:
            raise ValueError(
                f"Невозможно перемножить матрицы с размерностями {self.shape} и {other.shape}. "
                f"Количество столбцов первой матрицы ({self.shape[1]}) должно совпадать "
                f"с количеством строк второй матрицы ({other.shape[0]})"
            )

        return Matrix(self.data @ other.data)

    def __repr__(self):
        return f"Matrix({self.shape[0]}x{self.shape[1]}):\n{self.data}"

    def __str__(self):
        return str(self.data)

    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt='%d')

import numpy as np


class HashMixin:
    def __hash__(self):
        # сумма всех элементов матрицы
        return int(np.sum(self.data))

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False
        return np.array_equal(self.data, other.data)


class Matrix:
    _cache = {}

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
            )

        cache_key = (hash(self), hash(other))
        if cache_key in Matrix._cache:
            return Matrix._cache[cache_key]

        result = Matrix(self.data @ other.data)
        Matrix._cache[cache_key] = result
        return result

    def __repr__(self):
        return f"Matrix({self.shape[0]}x{self.shape[1]}):\n{self.data}"

    def __str__(self):
        return str(self.data)

    def save_to_file(self, filename):
        np.savetxt(filename, self.data, fmt='%d')

    def __hash__(self):
        return HashMixin.__hash__(self)

    def __eq__(self, other):
        return HashMixin.__eq__(self, other)

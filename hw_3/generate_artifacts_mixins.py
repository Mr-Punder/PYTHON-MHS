import numpy as np
from matrix_mixins import Matrix


def main():
    np.random.seed(0)

    matrix1_data = np.random.randint(0, 10, (10, 10))
    matrix2_data = np.random.randint(0, 10, (10, 10))

    matrix1 = Matrix(matrix1_data)
    matrix2 = Matrix(matrix2_data)

    result_add = matrix1 + matrix2
    result_mul = matrix1 * matrix2
    result_matmul = matrix1 @ matrix2

    with open("hw_3/3.2.txt", "w") as f:
        f.write("matrix1:\n")
        np.savetxt(f, matrix1.data, fmt='%d')
        f.write("\nmatrix2:\n")
        np.savetxt(f, matrix2.data, fmt='%d')
        f.write("\nmatrix1 + matrix2:\n")
        np.savetxt(f, result_add.data, fmt='%d')
        f.write("\nmatrix1 * matrix2:\n")
        np.savetxt(f, result_mul.data, fmt='%d')
        f.write("\nmatrix1 @ matrix2:\n")
        np.savetxt(f, result_matmul.data, fmt='%d')


if __name__ == "__main__":
    main()

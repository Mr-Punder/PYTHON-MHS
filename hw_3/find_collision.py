import numpy as np
from matrix_hash import Matrix


def find_collision():
    np.random.seed(42)

    while True:
        A_data = np.random.randint(0, 10, (3, 3))
        A = Matrix(A_data)

        C_data = A_data.copy()
        if C_data[0, 0] > 0 and C_data[0, 1] < 9:
            C_data[0, 0] -= 1
            C_data[0, 1] += 1
        elif C_data[0, 0] < 9 and C_data[0, 1] > 0:
            C_data[0, 0] += 1
            C_data[0, 1] -= 1
        else:
            continue

        C = Matrix(C_data)

        if hash(A) == hash(C) and not np.array_equal(A.data, C.data):
            return A, C


if __name__ == "__main__":
    A, C = find_collision()
    print(f"Found collision!")
    print(f"A:\n{A}")
    print(f"C:\n{C}")
    print(f"hash(A) = {hash(A)}")
    print(f"hash(C) = {hash(C)}")
    print(f"A == C: {A == C}")

import numpy as np
from matrix_hash import Matrix


def main():
    A_data = np.array([
        [6, 3, 7],
        [4, 6, 9],
        [2, 6, 4]
    ])
    A = Matrix(A_data)

    C_data = np.array([
        [5, 4, 7],
        [4, 6, 9],
        [2, 6, 4]
    ])
    C = Matrix(C_data)

    B_data = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    B = Matrix(B_data)
    D = Matrix(B_data)

    Matrix._cache.clear()
    AB = A @ B

    Matrix._cache.clear()
    CD_real = Matrix(C.data @ D.data)

    A.save_to_file("hw_3/A.txt")
    B.save_to_file("hw_3/B.txt")
    C.save_to_file("hw_3/C.txt")
    D.save_to_file("hw_3/D.txt")
    AB.save_to_file("hw_3/AB.txt")
    CD_real.save_to_file("hw_3/CD.txt")

    with open("hw_3/hash.txt", "w") as f:
        f.write(f"hash(A) = {hash(A)}\n")
        f.write(f"hash(C) = {hash(C)}\n")
        f.write(f"hash(AB) = {hash(AB)}\n")
        f.write(f"hash(CD) = {hash(CD_real)}\n")


if __name__ == "__main__":
    main()

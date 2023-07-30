import numpy as np

def input_matrix():
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    matrix_elements = []

    for i in range(cols):
        row_input = input(f"Enter elements for row {i+1} separated by space: ")
        row_elements = [int(x) for x in row_input.split()]
        matrix_elements.append(row_elements)

    matrix = np.array(matrix_elements)
    return matrix

def input_matrix2():
    rows2 = int(input("Enter the number of rows: "))
    cols2 = int(input("Enter the number of columns: "))

    matrix_elements2 = []

    for i in range(cols2):
        row2_input = input(f"Enter elements for row {i+1} separated by space: ")
        row2_elements = [int(x) for x in row2_input.split()]
        matrix_elements2.append(row2_elements)

    matrix2 = np.array(matrix_elements2)
    return matrix2

def add_matrices():
    a = input_matrix()
    b = input_matrix2()

    if a.shape != b.shape:
        print("Matrix addition is not possible. The dimensions of the matrices are different.")
        return None, None, None

    result_add = a + b
    return result_add, a, b


def transpose_matrices():
    matrix = input_matrix()
    matrix2 = input_matrix2()
    a = np.transpose(matrix)
    b = np.transpose(matrix2)
    return a, b

if __name__ == "__main__":
    user_matrix = input_matrix()
    user_matrix2 = input_matrix2()
    while True:
        add, transposed_matrix, transposed_matrix2 = add_matrices()
        if add is not None:
            print("Matrix A:")
            print(user_matrix)
            print("Matrix B:")
            print(user_matrix2)
            print("Addition of matrices:")
            print(add)
            print("Transpose of Matrix A:")
            print(transposed_matrix.T)  # Transpose matrix A
            print("Transpose of Matrix B:")
            print(transposed_matrix2.T)  # Transpose matrix B
        else:
            print("Matrix addition was not performed.")
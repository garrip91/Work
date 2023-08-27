import numpy as np


class Matrix:
    
    def __init__(self, matrix):
        self.matrix = matrix
        self.np_matrix = np.array(matrix)
    
    def __add__(self, other):
        return Matrix(self.np_matrix + other.np_matrix)
    
    def __str__(self) -> str:
        self.np_matrix = self.np_matrix.tolist()
        result_str = ""
        for i in self.np_matrix:
            internal_list = []
            for j in i:
                internal_list.append(str(j))
            result_str += f"{' '.join(internal_list)}\n"
        #return result_str[:-1]
        return f"Результирующая матрица:\n{result_str[:-1]}"


matrix_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix_2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print(matrix_1 + matrix_2)

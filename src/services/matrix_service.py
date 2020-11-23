import numpy as np

class MatrixService:
    def __init__(self, root):
        self.root = root
        self.matrix_a = []
        self.matrix_b = []
        self.result = []

    def return_values_to_service_a(self, matrix_a):
        self.matrix_a = np.array(matrix_a)
        return self.matrix_a

    def return_values_to_service_b(self, matrix_b):
        self.matrix_b = np.array(matrix_b)
        return self.matrix_b

    def transpose_matrix_a(self):
        return self.matrix_a.transpose()

    def transpose_matrix_b(self):
        return self.matrix_b.transpose()

    def determinant_matrix_a(self):
        return np.linalg.det(self.matrix_a)

    def determinant_matrix_b(self):
        return np.linalg.det(self.matrix_b)

    def inverse_matrix_a(self):
        try:
            mat_inv_a = np.linalg.inv(self.matrix_a)
            return mat_inv_a
        except:
            return "Not Invertible"

    def inverse_matrix_b(self):
        try:
            mat_inv_b = np.linalg.inv(self.matrix_b)
            return mat_inv_b
        except:
            return "Not Invertible"

    def multiply_matrix_a_by(self, multiplier):
        return multiplier*self.matrix_a

    def power_of_matrix_a(self, exp):
        return np.linalg.matrix_power(self.matrix_a, exp)

    def power_of_matrix_b(self, exp):
        return np.linalg.matrix_power(self.matrix_b, exp)

    def multiply_matrix_b_by(self, multiplier):
        return multiplier*self.matrix_b

    def a_mul_b(self):
        return self.matrix_a @ self.matrix_b

    def a_plus_b(self):
        return self.matrix_a + self.matrix_b

    def a_minus_b(self):
        return self.matrix_a - self.matrix_b

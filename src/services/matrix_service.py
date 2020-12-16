import numpy as np

class MatrixService:
    """Class responsible of matrix calculation services
    """
    def __init__(self):
        self.matrix_a = []
        self.matrix_b = []
        """Constructor of the Class. Creates two empty lists.
        """

    def return_values_to_service_a(self, matrix_a):
        """Returns values from MainView class from matrix A

        Args:
            matrix_a (list): List of values from matrix A

        Returns:
            np.array: Numpy array list
        """
        self.matrix_a = np.array(matrix_a)
        return self.matrix_a

    def return_values_to_service_b(self, matrix_b):
        """Returns values from MainView class from matrix B

        Args:
            matrix_a (list): List of values from matrix B

        Returns:
            np.array: Numpy array list
        """
        self.matrix_b = np.array(matrix_b)
        return self.matrix_b

    def transpose_matrix_a(self):
        """Calculates transpose of matrix A and returns result

        Returns:
            np.array: Numpy array list
        """
        return self.matrix_a.transpose()

    def transpose_matrix_b(self):
        """Calculates transpose of matrix B and returns result

        Returns:
            np.array: Numpy array list
        """
        return self.matrix_b.transpose()

    def determinant_matrix_a(self):
        """Calculates determinant of matrix A and returns result

        Returns:
            float: Float number
        """
        return np.linalg.det(self.matrix_a)

    def determinant_matrix_b(self):
        """Calculates determinant of matrix B and returns result

        Returns:
            float: Float number
        """
        return np.linalg.det(self.matrix_b)

    def inverse_matrix_a(self):
        """Calculates and returns inverse of matrix A if possible else returns
            empty list

        Returns:
            np.array: Numpy array list
        """
        try:
            mat_inv_a = np.linalg.inv(self.matrix_a)
            return mat_inv_a
        except np.linalg.LinAlgError:
            return []

    def inverse_matrix_b(self):
        """Calculates and returns inverse of matrix B if possible else returns
            empty list

        Returns:
            np.array: Numpy array list
        """
        try:
            mat_inv_b = np.linalg.inv(self.matrix_b)
            return mat_inv_b
        except np.linalg.LinAlgError:
            return []

    def multiply_matrix_a_by(self, multiplier):
        """Multiplies matrix A with a float number and returns result

        Args:
            multiplier (float): Float number for multiplication

        Returns:
            np.array: Numpy array list
            str: String
        """
        return multiplier*self.matrix_a

    def power_of_matrix_a(self, exp):
        """Calculates power of Integer number Matrix A and return results

        Args:
            exp (int): Integer number for calculation

        Returns:
            np.array: Numpy array list
        """
        return np.linalg.matrix_power(self.matrix_a, exp)

    def power_of_matrix_b(self, exp):
        """Calculates power of Integer number Matrix B and return results

        Args:
            exp (int): Integer number for calculation

        Returns:
            np.array: Numpy array list
        """
        return np.linalg.matrix_power(self.matrix_b, exp)

    def multiply_matrix_b_by(self, multiplier):
        """Multiplies matrix B with a float number and returns result

        Args:
            multiplier (float): Float number for multiplication

        Returns:
            np.array: Numpy array list
        """
        return multiplier*self.matrix_b

    def a_mul_b(self):
        """Multiplies Matrix A with Matrix B and returns result

        Returns:
            np.array: Numpy array list
        """
        return self.matrix_a @ self.matrix_b

    def a_plus_b(self):
        """Adds Matrix A with Matrix B and returns result

        Returns:
            np.array: Numpy array list
        """
        return self.matrix_a + self.matrix_b

    def a_minus_b(self):
        """Substracts Matrix B from Matrix A and return result

        Returns:
            np.array: Numpy array list
        """
        return self.matrix_a - self.matrix_b

matrix_service = MatrixService()

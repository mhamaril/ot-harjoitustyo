import unittest
import numpy as np
from tkinter import Tk

from services.matrix_service import MatrixService

class TestMatrixService(unittest.TestCase):

    def setUp(self):
        self.matrix_service = MatrixService()
        self.matrix_service.matrix_a = np.array(
            [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
        self.matrix_service.matrix_b = np.array(
            [[9.0, 8.0, 7.0], [6.0, 5.0, 4.0], [3.0, 2.0, 1.0]])
        self.multiplier = 2
        self.exp = 2
        self.result = []

    def test_return_values_to_service_a(self):
        result = self.matrix_service.return_values_to_service_a(
            [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
        self.assertTrue(
            (result == np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])).all())

    def test_return_values_to_service_b(self):
        result = self.matrix_service.return_values_to_service_b(
            [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
        self.assertTrue(
            (result == np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])).all())

    def test_axb_works_correctly(self):
        result = self.matrix_service.a_mul_b()
        self.assertTrue((result == np.array(
            [[30, 24, 18], [84, 69, 54], [138, 114, 90]])).all())

    def test_matrix_add_works_correctly(self):
        result = self.matrix_service.a_plus_b()
        self.assertTrue((result == np.array(
            [[10.0, 10.0, 10.0], [10.0, 10.0, 10.0], [10.0, 10.0, 10.0]])).all())

    def test_matrix_subtract_works_correctly(self):
        result = self.matrix_service.a_minus_b()
        self.assertTrue((result == np.array(
            [[-8.0, -6.0, -4.0], [-2.0, 0.0, 2.0], [4.0, 6.0, 8.0]])).all())

    def test_multiply_by_matrix_A_works_correctly(self):
        result = self.matrix_service.multiply_matrix_a_by(self.multiplier)
        self.assertTrue((result == np.array(
            [[2.0, 4.0, 6.0], [8.0, 10.0, 12.0], [14.0, 16.0, 18.0]])).all())

    def test_multiply_by_matrix_B_works_correctly(self):
        result = self.matrix_service.multiply_matrix_b_by(self.multiplier)
        self.assertTrue((result == np.array(
            [[18.0, 16.0, 14.0], [12.0, 10.0, 8.0], [6.0, 4.0, 2.0]])).all())

    def test_a_mul_b_works_correctly(self):
        result = self.matrix_service.a_mul_b()
        self.assertTrue((result == np.array(
            [[30.0, 24.0, 18.0], [84.0, 69.0, 54.0], [138.0, 114.0, 90.0]])).all())

    def test_a_plus_b_works_correctly(self):
        result = self.matrix_service.a_plus_b()
        self.assertTrue((result == np.array(
            [[10.0, 10.0, 10.0], [10.0, 10.0, 10.0], [10.0, 10.0, 10.0]])).all())

    def test_a_minus_b_works_correctly(self):
        result = self.matrix_service.a_minus_b()
        self.assertTrue((result == np.array(
            [[-8.0, -6.0, -4.0], [-2.0, 0.0, 2.0], [4.0, 6.0, 8.0]])).all())

    def test_transpose_matrix_a_works_correctly(self):
        result = self.matrix_service.transpose_matrix_a()
        self.assertTrue((result == np.array(
            [[1.0, 4.0, 7.0], [2.0, 5.0, 8.0], [3.0, 6.0, 9.0]])).all())

    def test_transpose_matrix_b(self):
        result = self.matrix_service.transpose_matrix_b()
        self.assertTrue((result == np.array(
            [[9.0, 6.0, 3.0], [8.0, 5.0, 2.0], [7.0, 4.0, 1.0]])).all())

    def test_determinant_matrix_a_works_correctly(self):
        result = self.matrix_service.determinant_matrix_a()
        self.assertEqual(result, 0.0)

    def test_determinant_matrix_b_works_correctly(self):
        result = self.matrix_service.determinant_matrix_b()
        self.assertEqual(result, 0.0)

    def test_inverse_matrix_a_works_correctly(self):
        self.matrix_service.matrix_a = np.array(
            [[1.0, 2.0, 1.0], [2.0, 1.0, 2.0], [1.0, 1.0, 2.0]])
        result = self.matrix_service.inverse_matrix_a()
        self.assertTrue((result == np.array(
            [[0.0, 1.0, -1.0], [float(2/3), float(-1/3), 0.0], 
            [float(-1/3), float(-1/3), 1.0]])).any())

    def test_inverse_matrix_b(self):
        self.matrix_service.matrix_b = np.array(
            [[1.0, 2.0, 1.0], [2.0, 1.0, 2.0], [1.0, 1.0, 2.0]])
        result = self.matrix_service.inverse_matrix_b()
        self.assertTrue((result == np.array(
            [[0.0, 1.0, -1.0], [float(2/3), float(-1/3), 0.0], 
            [float(-1/3), float(-1/3), 1.0]])).any())
    
    def test_matrix_a_not_invertible(self):
        result = self.matrix_service.inverse_matrix_a()
        self.assertRaises(np.linalg.LinAlgError)
        self.assertEqual(result, [])
    
    def test_matrix_b_not_invertible(self):
        result = self.matrix_service.inverse_matrix_a()
        self.assertRaises(np.linalg.LinAlgError)
        self.assertEqual(result, [])
    


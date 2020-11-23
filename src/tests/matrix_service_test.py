import unittest
import numpy as np
from tkinter import Tk

from services.matrix_service import MatrixService
from gui.main_view import MainView

class TestMatrixService(unittest.TestCase):
    
    def setUp(self):
        window = Tk()
        self.root = MainView(window, "Matrix Calculator")
        self.root.a11.insert(0, 1)
        self.root.a12.insert(0, 2)
        self.root.a13.insert(0, 3)
        self.root.a21.insert(0, 4)
        self.root.a22.insert(0, 5)
        self.root.a23.insert(0, 6)
        self.root.a31.insert(0, 7)
        self.root.a32.insert(0, 8)
        self.root.a33.insert(0, 9)

        self.root.b11.insert(0, 9)
        self.root.b12.insert(0, 8)
        self.root.b13.insert(0, 7)
        self.root.b21.insert(0, 6)
        self.root.b22.insert(0, 5)
        self.root.b23.insert(0, 4)
        self.root.b31.insert(0, 3)
        self.root.b32.insert(0, 2)
        self.root.b33.insert(0, 1)

        self.root.m_b_a.insert(0, 2)
        self.root.p_o_a.insert(0, 2)
        self.root.m_b_b.insert(0, 2)
        self.root.p_o_b.insert(0, 2)

        
        #self.root = MainView(window, "Matrix Calculator")
        self.matrix_service = MatrixService(self.root)
        self.matrix_service.matrix_a = np.array([[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]])
        self.matrix_service.matrix_b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0], [3.0, 2.0, 1.0]])
        self.multiplier = 2
        self.exp = 2
        self.result = []
    
    

    def test_AxB_works_correctly(self):
        result = self.matrix_service.a_mul_b()
        self.assertEqual(result, np.array([[30, 24, 18], [84, 69, 54], [138, 114, 90]]))

    def test_matrix_add_works_correctly(self):
        result = self.matrix_service.a_plus_b()
        self.assertEqual(result, np.array([[10.0, 10.0, 10.0], [10.0, 10.0, 10.0], [10.0, 10.0, 10.0]]))

    def test_matrix_subtract_works_correctly(self):
        result = self.matrix_service.a_minus_b()
        self.assertEqual(result, np.array([[-8.0, -6.0, -4.0], [-2.0, 0.0, 2.0], [4.0, 6.0, 8.0]]))

    def test_multiply_by_matrix_A(self):
        result = self.matrix_service.multiply_matrix_a_by(self.multiplier)
        self.assertEqual(result, np.array([[2.0, 4.0, 6.0], [8.0, 10.0, 12.0], [14.0, 16.0, 18.0]]))

    def test_multiply_by_matrix_B(self):
        result = self.matrix_service.multiply_matrix_a_by(self.multiplier)
        self.assertEqual(result, np.array([[18.0, 16.0, 14.0], [12.0, 10.0, 8.0], [6.0, 4.0, 2.0]]))

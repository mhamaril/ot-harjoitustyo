import unittest
from tkinter import Tk
import numpy as np
from gui.main_view import MainView



class TestMainView(unittest.TestCase):
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

        self.root.mbA.insert(0, 2)
        self.root.poA.insert(0, 2)
        self.root.mbB.insert(0, 2)
        self.root.poB.insert(0, 2)

    def test_flip_matrices_work_correctly(self):
        self.root.flip_matrices()
        self.assertEqual([[float(self.root.a11.get()), float(self.root.a12.get()), float(self.root.a13.get())], [float(self.root.a21.get()), float(self.root.a22.get()), float(
            self.root.a23.get())], [float(self.root.a31.get()), float(self.root.a32.get()), float(self.root.a33.get())]], [[9.0, 8.0, 7.0], [6.0, 5.0, 4.0], [3.0, 2.0, 1.0]])

    def test_AxB_works_correctly(self):
        result = self.root.matrix_multiply()
        self.assertEqual([[float(self.root.r11.get()), float(self.root.r12.get()), float(self.root.r13.get())], [float(self.root.r21.get()), float(self.root.r22.get()), float(self.root.r23.get())], [float(
            self.root.r31.get()), float(self.root.r32.get()), float(self.root.r33.get())]], [[30.0, 24.0, 18.0], [84.0, 69.0, 54.0], [138.0, 114.0, 90.0]], np.array([[30, 24, 18], [84, 69, 54], [138, 114, 90]]))

    def test_matrix_add_works_correctly(self):
        result = self.root.matrix_add()
        self.assertEqual([[float(self.root.r11.get()), float(self.root.r12.get()), float(self.root.r13.get())], [float(self.root.r21.get()), float(self.root.r22.get()), float(
            self.root.r23.get())], [float(self.root.r31.get()), float(self.root.r32.get()), float(self.root.r33.get())]], [[10.0, 10.0, 10.0], [10.0, 10.0, 10.0], [10.0, 10.0, 10.0]])

    def test_matrix_subtract_works_correctly(self):
        result = self.root.matrix_subtract()
        self.assertEqual([[float(self.root.r11.get()), float(self.root.r12.get()), float(self.root.r13.get())], [float(self.root.r21.get()), float(self.root.r22.get()), float(
            self.root.r23.get())], [float(self.root.r31.get()), float(self.root.r32.get()), float(self.root.r33.get())]], [[-8.0, -6.0, -4.0], [-2.0, 0.0, 2.0], [4.0, 6.0, 8.0]])

    def test_multiply_by_matrix_A(self):
        result = self.root.multiply_by_matrix_A()
        self.assertEqual([[float(self.root.r11.get()), float(self.root.r12.get()), float(self.root.r13.get())], [float(self.root.r21.get()), float(self.root.r22.get()), float(
            self.root.r23.get())], [float(self.root.r31.get()), float(self.root.r32.get()), float(self.root.r33.get())]], [[2.0, 4.0, 6.0], [8.0, 10.0, 12.0], [14.0, 16.0, 18.0]])

    def test_multiply_by_matrix_B(self):
        result = self.root.multiply_by_matrix_B()
        self.assertEqual([[float(self.root.r11.get()), float(self.root.r12.get()), float(self.root.r13.get())], [float(self.root.r21.get()), float(self.root.r22.get()), float(
            self.root.r23.get())], [float(self.root.r31.get()), float(self.root.r32.get()), float(self.root.r33.get())]], [[18.0, 16.0, 14.0], [12.0, 10.0, 8.0], [6.0, 4.0, 2.0]])

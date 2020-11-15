import unittest
from gui.main_view import MainView
from tkinter import Tk

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
        
    def test_does_flip_matrices_work_correctly(self):
        self.root.flip_matrices()
        self.assertEqual([[float(self.root.a11.get()),float(self.root.a12.get()),float(self.root.a13.get())],[float(self.root.a21.get()), float(self.root.a22.get()), float(self.root.a23.get())],[float(self.root.a31.get()),float(self.root.a32.get()),float(self.root.a33.get())]], [[9.0,8.0,7.0],[6.0,5.0,4.0],[3.0,2.0,1.0]])

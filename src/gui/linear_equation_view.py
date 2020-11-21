from tkinter import *
import numpy as np


class LinearEquationView():
    def __init__(self, root, title):
        self.root = root
        self.title = title

    def initialize_view(self):
        self.root.title(self.title)
        pass

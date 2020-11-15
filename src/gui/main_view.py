from tkinter import *
import numpy as np



class MainView:
    def __init__(self, root, title):
        self.root = root
        self.title = title
        self.initialize_view()

    def initialize_view(self):
        self.root.title(self.title)
        matrixA = Label(self.root, text="Matrix A")
        matrixB = Label(self.root, text="Matrix B")

        matrixA.grid(row=0, column=1)
        matrixB.grid(row=0, column=8)

        self.a11 = Entry(self.root, width= 9, borderwidth=5)
        self.a11.grid(row=1, column=0)
        self.a12 = Entry(self.root, width= 9, borderwidth=5)
        self.a12.grid(row=1, column=1)
        self.a13 = Entry(self.root, width= 9, borderwidth=5)
        self.a13.grid(row=1, column=2)
        self.a21 = Entry(self.root, width= 9, borderwidth=5)
        self.a21.grid(row=2, column=0)
        self.a22 = Entry(self.root, width= 9, borderwidth=5)
        self.a22.grid(row=2, column=1)
        self.a23 = Entry(self.root, width= 9, borderwidth=5)
        self.a23.grid(row=2, column=2)
        self.a31 = Entry(self.root, width= 9, borderwidth=5)
        self.a31.grid(row=3, column=0)
        self.a32 = Entry(self.root, width= 9, borderwidth=5)
        self.a32.grid(row=3, column=1)
        self.a33 = Entry(self.root, width= 9, borderwidth=5)
        self.a33.grid(row=3, column=2)
        
        self.b11 = Entry(self.root, width= 9, borderwidth=5)
        self.b11.grid(row=1, column=7)
        self.b12 = Entry(self.root, width= 9, borderwidth=5)
        self.b12.grid(row=1, column=8)
        self.b13 = Entry(self.root, width= 9, borderwidth=5)
        self.b13.grid(row=1, column=9)
        self.b21 = Entry(self.root, width= 9, borderwidth=5)
        self.b21.grid(row=2, column=7)
        self.b22 = Entry(self.root, width= 9, borderwidth=5)
        self.b22.grid(row=2, column=8)
        self.b23 = Entry(self.root, width= 9, borderwidth=5)
        self.b23.grid(row=2, column=9)
        self.b31 = Entry(self.root, width= 9, borderwidth=5)
        self.b31.grid(row=3, column=7)
        self.b32 = Entry(self.root, width= 9, borderwidth=5)
        self.b32.grid(row=3, column=8)
        self.b33 = Entry(self.root, width= 9, borderwidth=5)
        self.b33.grid(row=3, column=9)
        self.root.grid_columnconfigure(4, minsize=100)
        self.root.grid_columnconfigure(6, minsize=100)

        button_inverse = Button(self.root, text="Inv(A)", width=7, command=self.inverse)
        button_inverse.grid(row=6, column=1)
        button_transpose = Button(self.root, text="Trans(A)", width=7, command=self.transpose_matrixA)
        button_transpose.grid(row=6, column=0)
        button_determinant = Button(self.root, text="Det(A)", width=7, command=self.determinant)
        button_determinant.grid(row=6, column=2)
        button_AxB = Button(self.root, text="A x B", width=7, command=self.matrix_multiply)
        button_AxB.grid(row = 3, column=5)
        button_A_add_B = Button(self.root, text="A + B", width=7, command=self.matrix_add)
        button_A_add_B.grid(row = 4, column=5)
        button_A_subs_B = Button(self.root, text="A - B", width=7, command=self.matrix_subtract)
        button_A_subs_B.grid(row = 5, column=5)
        button_flip_matrices= Button(self.root, text="Flip", width=7, command=self.flip_matrices)
        button_flip_matrices.grid(row = 1, column=5)
        button_clearA = Button(self.root, text="Clear", width=7, command=self.clearA)
        button_clearA.grid(row=4, column=0)
        button_size_up_matrixA = Button(self.root, text="+", width=7)
        button_size_up_matrixA.grid(row=4, column=1)
        button_size_down_matrixA = Button(self.root, text="-", width=7)
        button_size_down_matrixA.grid(row=4, column=2)
        button_clearB = Button(self.root, text="Clear", width=7, command=self.clearB)
        button_clearB.grid(row=4, column=7)
        button_size_up_matrixB = Button(self.root, text="+", width=7)
        button_size_up_matrixB.grid(row=4, column=8)
        button_size_down_matrixB = Button(self.root, text="-", width=7)
        button_size_down_matrixB.grid(row=4, column=9)

    def inverse(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrixInvLabel = Label(self.root, text=matrixA)
        matrixInvLabel.grid(row = 9, column=5)

    def transpose_matrixA(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrixTrans = matrixA.transpose()
        matrixTransLabel = Label(self.root, text=matrixTrans)
        matrixTransLabel.grid(row = 9, column=5)
        return matrixTrans

    def determinant(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrix_detA = np.linalg.det(matrixA)
        matrixDet= Label(self.root, text="      \n       \n       \n         \n       ")
        matrixDet= Label(self.root, text=matrix_detA)
        matrixDet.grid(row=9, column=5)

    def matrix_multiply(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrixB = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        multiplication = np.matmul(matrixA, matrixB)
        matrixMul= Label(self.root, text="")
        matrixMul= Label(self.root, text=multiplication)
        matrixMul.grid(row=9, column=5)

    def matrix_add(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrixB = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        matrixAddition = matrixA + matrixB
        matrixAdditionLabel = Label(self.root, text=matrixAddition)
        matrixAdditionLabel.grid(row=9, column=5)
    

    def matrix_subtract(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrixB = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        matrixSubstraction = matrixA - matrixB
        matrixSubstractionLabel = Label(self.root, text=matrixSubstraction)
        matrixSubstractionLabel.grid(row=9, column=5)

    def flip_matrices(self):
        temp = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        self.b11.delete(0, END)
        self.b12.delete(0, END)
        self.b13.delete(0, END)
        self.b21.delete(0, END)
        self.b22.delete(0, END)
        self.b22.delete(0, END)
        self.b23.delete(0, END)
        self.b31.delete(0, END)
        self.b32.delete(0, END)
        self.b33.delete(0, END)
        self.b11.insert(0, float(self.a11.get()))
        self.b12.insert(0, float(self.a12.get()))
        self.b13.insert(0, float(self.a13.get()))
        self.b21.insert(0, float(self.a21.get()))
        self.b22.insert(0, float(self.a22.get()))
        self.b23.insert(0, float(self.a23.get()))
        self.b31.insert(0, float(self.a31.get()))
        self.b32.insert(0, float(self.a32.get()))
        self.b33.insert(0, float(self.a33.get()))

        self.a11.delete(0, END)
        self.a12.delete(0, END)
        self.a13.delete(0, END)
        self.a21.delete(0, END)
        self.a22.delete(0, END)
        self.a23.delete(0, END)
        self.a31.delete(0, END)
        self.a32.delete(0, END)
        self.a33.delete(0, END)
        self.a11.insert(0, temp[0][0])
        self.a12.insert(0, temp[0][1])
        self.a13.insert(0, temp[0][2])
        self.a21.insert(0, temp[1][0])
        self.a22.insert(0, temp[1][1])
        self.a23.insert(0, temp[1][2])
        self.a31.insert(0, temp[2][0])
        self.a32.insert(0, temp[2][1])
        self.a33.insert(0, temp[2][2])
    
    def clearA(self):
        self.a11.delete(0, END)
        self.a12.delete(0, END)
        self.a13.delete(0, END)
        self.a21.delete(0, END)
        self.a22.delete(0, END)
        self.a23.delete(0, END)
        self.a31.delete(0, END)
        self.a32.delete(0, END)
        self.a33.delete(0, END)

    def clearB(self):
        self.b11.delete(0, END)
        self.b12.delete(0, END)
        self.b13.delete(0, END)
        self.b21.delete(0, END)
        self.b22.delete(0, END)
        self.b22.delete(0, END)
        self.b23.delete(0, END)
        self.b31.delete(0, END)
        self.b32.delete(0, END)
        self.b33.delete(0, END)

    
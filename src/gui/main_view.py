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

        button_inverse_A = Button(self.root, text="Inv(A)", width=7, command=self.inverse_matrix_A)
        button_inverse_A.grid(row=6, column=1)
        button_transpose_A = Button(self.root, text="Trans(A)", width=7, command=self.transpose_matrix_A)
        button_transpose_A.grid(row=6, column=0)
        button_determinant_A = Button(self.root, text="Det(A)", width=7, command=self.determinant_matrix_A)
        button_determinant_A.grid(row=6, column=2)

        button_multiply_by_A = Button(self.root, text="Multiply by", width=17, command=self.multiply_by_matrix_A)
        button_multiply_by_A.grid(row=7, column=0, columnspan=2)
        self.mbA = Entry(self.root, width= 9, borderwidth=5)
        self.mbA.grid(row=7, column=2)

        button_multiply_by_B = Button(self.root, text="Multiply by", width=17, command=self.multiply_by_matrix_B)
        button_multiply_by_B.grid(row=7, column=7, columnspan=2)
        self.mbB = Entry(self.root, width= 9, borderwidth=5)
        self.mbB.grid(row=7, column=9)

        button_power_of_A = Button(self.root, text="Raise to power of", width=17, command=self.power_of_matrix_A)
        button_power_of_A.grid(row=8, column=0, columnspan=2)
        self.poA = Entry(self.root, width= 9, borderwidth=5)
        self.poA.grid(row=8, column=2)

        button_power_of_B = Button(self.root, text="Raise to power of", width=17, command=self.power_of_matrix_B)
        button_power_of_B.grid(row=8, column=7, columnspan=2)
        self.poB = Entry(self.root, width= 9, borderwidth=5)
        self.poB.grid(row=8, column=9)

        button_inverse_B = Button(self.root, text="Inv(B)", width=7, command=self.inverse_matrix_B)
        button_inverse_B.grid(row=6, column=8)
        button_transpose_B = Button(self.root, text="Trans(B)", width=7, command=self.transpose_matrix_B)
        button_transpose_B.grid(row=6, column=7)
        button_determinant_B = Button(self.root, text="Det(B)", width=7, command=self.determinant_matrix_B)
        button_determinant_B.grid(row=6, column=9)

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

        result_entry = Label(self.root, text="Result")
        result_entry.grid(row=11, column=5)
        self.r11 = Entry(self.root, width= 9, borderwidth=5)
        self.r11.grid(row=12, column=4)
        self.r12 = Entry(self.root, width= 9, borderwidth=5)
        self.r12.grid(row=12, column=5)
        self.r13 = Entry(self.root, width= 9, borderwidth=5)
        self.r13.grid(row=12, column=6)
        self.r21 = Entry(self.root, width= 9, borderwidth=5)
        self.r21.grid(row=13, column=4)
        self.r22 = Entry(self.root, width= 9, borderwidth=5)
        self.r22.grid(row=13, column=5)
        self.r23 = Entry(self.root, width= 9, borderwidth=5)
        self.r23.grid(row=13, column=6)
        self.r31 = Entry(self.root, width= 9, borderwidth=5)
        self.r31.grid(row=14, column=4)
        self.r32 = Entry(self.root, width= 9, borderwidth=5)
        self.r32.grid(row=14, column=5)
        self.r33 = Entry(self.root, width= 9, borderwidth=5)
        self.r33.grid(row=14, column=6)

        button_insert_in_A = Button(self.root, text="Insert in A", width=17, command=self.insert_result_in_A)
        button_insert_in_A.grid(row=12, column=7, columnspan=2)
        button_insert_in_B = Button(self.root, text="Insert in B", width=17, command=self.insert_result_in_B)
        button_insert_in_B.grid(row=13, column=7, columnspan=2)

    def inverse_matrix_A(self):
        matrix_A = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        try:
            mat_inv_A = np.linalg.inv(matrix_A)
            boolean = True
        except:
            mat_inv_A = []
            boolean = False
        
        self.result_function(mat_inv_A, boolean)
        
    def reset_results(self):
        self.r11.delete(0, END)
        self.r12.delete(0, END)
        self.r13.delete(0, END)
        self.r21.delete(0, END)
        self.r22.delete(0, END)
        self.r22.delete(0, END)
        self.r23.delete(0, END)
        self.r31.delete(0, END)
        self.r32.delete(0, END)
        self.r33.delete(0, END)

    def result_function(self, matrix, boolean):
        self.reset_results()
        if boolean == True:
            self.r11.insert(0, matrix[0][0])
            self.r12.insert(0, matrix[0][1])
            self.r13.insert(0, matrix[0][2])
            self.r21.insert(0, matrix[1][0])
            self.r22.insert(0, matrix[1][1])
            self.r23.insert(0, matrix[1][2])
            self.r31.insert(0, matrix[2][0])
            self.r32.insert(0, matrix[2][1])
            self.r33.insert(0, matrix[2][2])
        else:
            self.r12.insert(0, "   Not")
            self.r22.insert(0, "Invertible")

    def transpose_matrix_A(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrixTrans = matrixA.transpose()
        self.latest_result = matrixTrans
        self.result_function(matrixTrans, True)

    def determinant_matrix_A(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrix_detA = np.linalg.det(matrixA)
        self.reset_results()
        self.r22.insert(0, matrix_detA)
    
    def multiply_by_matrix_A(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        result_mul = matrixA*(float(self.mbA.get()))
        self.result_function(result_mul, True)
    
    def power_of_matrix_A(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        result_pow = np.linalg.matrix_power(matrixA, int(self.poA.get()))
        self.result_function(result_pow, True)

    def inverse_matrix_B(self):
        matrix_B = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        try:
            mat_inv_B = np.linalg.inv(matrix_B)
            boolean = True
        except:
            mat_inv_B = []
            boolean = False
        
        self.result_function(mat_inv_B, boolean)

    def transpose_matrix_B(self):
        matrix_B = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        matrixTrans = matrix_B.transpose()
        self.result_function(matrixTrans, True)

    def determinant_matrix_B(self):
        matrix_B = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        matrix_det_B = np.linalg.det(matrix_B)
        self.reset_results()
        self.r22.insert(0, matrix_det_B)
    
    def multiply_by_matrix_B(self):
        matrix_B = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        result_mul = matrix_B*(float(self.mbB.get()))
        self.result_function(result_mul, True)
    
    def power_of_matrix_B(self):
        matrix_B = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        result_pow = np.linalg.matrix_power(matrix_B, int(self.poB.get()))
        self.result_function(result_pow, True)

    def matrix_multiply(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrixB = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        multiplication = np.matmul(matrixA, matrixB)
        self.result_function(multiplication, True)

    def matrix_add(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrixB = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        matrixAddition = matrixA + matrixB
        self.result_function(matrixAddition, True)
    

    def matrix_subtract(self):
        matrixA = np.array([[float(self.a11.get()),float(self.a12.get()),float(self.a13.get())],[float(self.a21.get()), float(self.a22.get()), float(self.a23.get())],[float(self.a31.get()),float(self.a32.get()),float(self.a33.get())]])
        matrixB = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        matrixSubstraction = matrixA - matrixB
        self.result_function(matrixSubstraction, True)

    def flip_matrices(self):
        temp = np.array([[float(self.b11.get()),float(self.b12.get()),float(self.b13.get())],[float(self.b21.get()), float(self.b22.get()), float(self.b23.get())],[float(self.b31.get()),float(self.b32.get()),float(self.b33.get())]])
        self.clearB()
        self.b11.insert(0, float(self.a11.get()))
        self.b12.insert(0, float(self.a12.get()))
        self.b13.insert(0, float(self.a13.get()))
        self.b21.insert(0, float(self.a21.get()))
        self.b22.insert(0, float(self.a22.get()))
        self.b23.insert(0, float(self.a23.get()))
        self.b31.insert(0, float(self.a31.get()))
        self.b32.insert(0, float(self.a32.get()))
        self.b33.insert(0, float(self.a33.get()))

        self.clearA()
        self.a11.insert(0, temp[0][0])
        self.a12.insert(0, temp[0][1])
        self.a13.insert(0, temp[0][2])
        self.a21.insert(0, temp[1][0])
        self.a22.insert(0, temp[1][1])
        self.a23.insert(0, temp[1][2])
        self.a31.insert(0, temp[2][0])
        self.a32.insert(0, temp[2][1])
        self.a33.insert(0, temp[2][2])
    
    def insert_result_in_A():
        self.clearA()
        self.a11.insert(0, float(self.r11.get()))
        self.a12.insert(0, float(self.r12.get()))
        self.a13.insert(0, float(self.r13.get()))
        self.a21.insert(0, float(self.r21.get()))
        self.a22.insert(0, float(self.r22.get()))
        self.a23.insert(0, float(self.r23.get()))
        self.a31.insert(0, float(self.r31.get()))
        self.a32.insert(0, float(self.r32.get()))
        self.a33.insert(0, float(self.r33.get()))

    def insert_result_in_B():
        self.clearB()
        self.b11.insert(0, float(self.r11.get()))
        self.b12.insert(0, float(self.r12.get()))
        self.b13.insert(0, float(self.r13.get()))
        self.b21.insert(0, float(self.r21.get()))
        self.b22.insert(0, float(self.r22.get()))
        self.b23.insert(0, float(self.r23.get()))
        self.b31.insert(0, float(self.r31.get()))
        self.b32.insert(0, float(self.r32.get()))
        self.b33.insert(0, float(self.r33.get()))
    
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

    
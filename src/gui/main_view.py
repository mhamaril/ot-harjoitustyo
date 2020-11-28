from tkinter import *

from services.matrix_service import MatrixService


class MainView:
    def __init__(self, root, title):
        self.root = root
        self.title = title
        self.size = 3
        self.matrix_service = MatrixService()
        self.frame = Frame(master=self.root)
        self.matrix_a = []
        self.matrix_a_values = []
        self.matrix_b_values = []
        self.matrix_b = []
        self.matrix = [[]]
        self.result = []
        self.result_values = []
        self.initialize_view(self.size)

    def initialize_view(self, n):
        self.clear_view()
        self.root.title(self.title)
        matrix_a = Label(master=self.frame, text="Matrix A")
        matrix_b = Label(master=self.frame, text="Matrix B")
        matrix_a.grid(row=0, column=0)
        matrix_b.grid(row=0, column=8)
        self.create_matrix_a(n)
        self.create_matrix_b(n)
        self.create_result(n)
        button_inverse_a = Button(
            master=self.frame, text="Inv(A)", width=7, command=self.inverse_a)
        button_inverse_a.grid(row=9, column=1)
        button_transpose_a = Button(
            master=self.frame, text="Trans(A)", width=7, command=self.transpose_a)
        button_transpose_a.grid(row=9, column=0)
        button_determinant_a = Button(
            master=self.frame, text="Det(A)", width=7, command=self.determinant_a)
        button_determinant_a.grid(row=9, column=2)

        button_multiply_by_a = Button(
            master=self.frame, text="Multiply by", width=17, command=self.multiply_by_a)
        button_multiply_by_a.grid(row=10, column=0, columnspan=2)
        self.m_b_a = Entry(master=self.frame, width=9, borderwidth=5)
        self.m_b_a.grid(row=10, column=2)

        button_multiply_by_b = Button(
            master=self.frame, text="Multiply by", width=17, command=self.multiply_by_b)
        button_multiply_by_b.grid(row=10, column=8, columnspan=2)
        self.m_b_b = Entry(master=self.frame, width=9, borderwidth=5)
        self.m_b_b.grid(row=10, column=10)

        button_power_of_a = Button(
            master=self.frame, text="Raise to power of", width=17, command=self.power_of_a)
        button_power_of_a.grid(row=11, column=0, columnspan=2)
        self.p_o_a = Entry(master=self.frame, width=9, borderwidth=5)
        self.p_o_a.grid(row=11, column=2)

        button_power_of_b = Button(
            master=self.frame, text="Raise to power of", width=17, command=self.power_of_b)
        button_power_of_b.grid(row=11, column=8, columnspan=2)
        self.p_o_b = Entry(master=self.frame, width=9, borderwidth=5)
        self.p_o_b.grid(row=11, column=10)

        button_inverse_b = Button(
            master=self.frame, text="Inv(B)", width=7, command=self.inverse_b)
        button_inverse_b.grid(row=9, column=9)
        button_transpose_b = Button(
            master=self.frame, text="Trans(B)", width=7, command=self.transpose_b)
        button_transpose_b.grid(row=9, column=8)
        button_determinant_b = Button(
            master=self.frame, text="Det(B)", width=7, command=self.determinant_b)
        button_determinant_b.grid(row=9, column=10)

        button_axb = Button(master=self.frame, text="A x B", width=7,
                            command=self.axb)
        button_axb.grid(row=3, column=7)
        button_a_add_b = Button(master=self.frame, text="A + B",
                                width=7, command=self.a_add_b)
        button_a_add_b.grid(row=4, column=7)
        button_a_subs_b = Button(
            master=self.frame, text="A - B", width=7, command=self.a_subs_b)
        button_a_subs_b.grid(row=5, column=7)
        button_flip_matrices = Button(
            master=self.frame, text="Flip", width=7, command=self.flip_matrices)
        button_flip_matrices.grid(row=1, column=7)
        button_clear_a = Button(
            master=self.frame, text="Clear", width=7, command=self.clear_a)
        button_clear_a.grid(row=8, column=0)
        button_size_up_matrix_a = Button(master=self.frame, text="+", width=7, command=self.size_up)
        button_size_up_matrix_a.grid(row=8, column=1)
        button_size_down_matrix_a = Button(master=self.frame, text="-", width=7, command=self.size_down)
        button_size_down_matrix_a.grid(row=8, column=2)
        button_clear_b = Button(
            master=self.frame, text="Clear", width=7, command=self.clear_b)
        button_clear_b.grid(row=8, column=8)
        button_size_up_matrix_b = Button(master=self.frame, text="+", width=7, command=self.size_up)
        button_size_up_matrix_b.grid(row=8, column=9)
        button_size_down_matrix_b = Button(master=self.frame, text="-", width=7, command=self.size_down)
        button_size_down_matrix_b.grid(row=8, column=10)

        button_insert_in_a = Button(
            master=self.frame, text="Insert in A", width=17, command=self.insert_result_in_a)
        button_insert_in_a.grid(row=13, column=4, columnspan=2)
        button_insert_in_b = Button(
            master=self.frame, text="Insert in B", width=17, command=self.insert_result_in_b)
        button_insert_in_b.grid(row=21, column=4, columnspan=2)
        self.frame.pack()

    def create_matrix_a(self, n):
        self.matrix_a = []
        for i in range(n):
            row  = []
            for j in range(n):
                temp = Entry(master=self.frame, width=9, borderwidth=5)
                temp.grid(row=i+1, column=j)
                row.append(temp)  
            self.matrix_a.append(row)
        return self.matrix_a

    def create_matrix_b(self, n):
        self.matrix_b = []
        for i in range(n):
            row  = []
            for j in range(n):
                temp = Entry(master=self.frame, width=9, borderwidth=5)
                temp.grid(row=i+1, column=j+8)
                row.append(temp)
            self.matrix_b.append(row)
        return self.matrix_b
    
    def create_result(self, n):
        self.result= []
        for i in range(n):
            row  = []
            for j in range(n):
                temp = Entry(master=self.frame, width=9, borderwidth=5)
                temp.grid(row=i+14, column=j+4)
                row.append(temp)
            self.result.append(row)

    def transpose_a(self):
        matrix = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix)
        self.result_values = self.matrix_service.transpose_matrix_a()
        self.show_results()
    
    def transpose_b(self):
        matrix = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix)
        self.result_values = self.matrix_service.transpose_matrix_b()
        self.show_results()
    
    def determinant_a(self):
        matrix = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix)
        det = self.matrix_service.determinant_matrix_a()
        self.show_det_or_inv(det)
    
    def determinant_b(self):
        matrix = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix)
        self.show_det_or_inv(self.matrix_service.determinant_matrix_b())

    def inverse_a(self):
        matrix = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix)
        self.show_det_or_inv(self.matrix_service.inverse_matrix_a())
    
    def inverse_b(self):
        matrix = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix)
        self.show_det_or_inv(self.matrix_service.inverse_matrix_b())
    
    def multiply_by_a(self):
        matrix = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix)
        self.result_values = self.matrix_service.multiply_matrix_a_by(float(self.m_b_a.get()))
        self.show_results()

    def power_of_a(self):
        matrix = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix)
        self.result_values = self.matrix_service.power_of_matrix_a(int(self.p_o_a.get()))
        self.show_results()

    def power_of_b(self):
        matrix = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix)
        self.result_values = self.matrix_service.power_of_matrix_b(int(self.p_o_b.get()))
        self.show_results()

    def multiply_by_b(self):
        matrix = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix)
        self.result_values = self.matrix_service.multiply_matrix_b_by(float(self.m_b_b.get()))
        self.show_results()
    
    def axb(self):
        matrix_a = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix_a)
        matrix_b = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix_b)
        self.result_values = self.matrix_service.a_mul_b()
        self.show_results()
    
    def a_add_b(self):
        matrix_a = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix_a)
        matrix_b = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix_b)
        self.result_values = self.matrix_service.a_plus_b()
        self.show_results()
    
    def a_subs_b(self):
        matrix_a = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix_a)
        matrix_b = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix_b)
        self.result_values = self.matrix_service.a_minus_b()
        self.show_results()
    
    def flip_matrices(self):
        temp_a = self.get_values_from_matrix_a()
        temp_b = self.get_values_from_matrix_b()
        self.clear_a()
        for i in range(self.size):
            for j in range(self.size):
                self.matrix_a[i][j].insert(0, float(temp_a[i][j]))
        self.clear_b()
        for i in range(self.size):
            for j in range(self.size):
                self.matrix_b[i][j].insert(0, float(temp_b[i][j]))
        
    def insert_result_in_a(self):
        self.clear_a()
        for i in range(self.size):
            for j in range(self.size):
                self.matrix_a[i][j].insert(0, float(self.result_values[i][j]))

    def insert_result_in_b(self):
        self.clear_b()
        for i in range(self.size):
            for j in range(self.size):
                self.matrix_b[i][j].insert(0, float(self.result_values[i][j]))

    def get_values_from_matrix_a(self):
        self.matrix_a_values = []
        for value in self.matrix_a:
            row = []
            for x in value:
                row.append(float(x.get()))
            self.matrix_a_values.append(row)
        return self.matrix_a_values

    def get_values_from_matrix_b(self):
        self.matrix_b_values = []
        for value in self.matrix_b:
            row = []
            for x in value:
                row.append(float(x.get()))
            self.matrix_b_values.append(row)
        return self.matrix_b_values

    def show_results(self):
        self.reset_results()
        for i in range(self.size):
            for j in range(self.size):
                self.result[i][j].insert(0, float(self.result_values[i][j]))
        
    def show_det_or_inv(self, det):
        self.reset_results()
        if type(det) == str:
            self.result[0][1].insert(0, "      Not")
            self.result[1][1].insert(0, "  Invertible")
        else:
            self.result[1][1].insert(0, float(det))
    
    def reset_results(self):
        for value in self.result:
            for j in range(self.size):
                value[j].delete(0, END)
        
    def clear_a(self):
        for value in self.matrix_a:
            for j in range(self.size):
                value[j].delete(0, END)
        
    def clear_b(self):
        for value in self.matrix_b:
            for j in range(self.size):
                value[j].delete(0, END)
         
    def clear_view(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()
        
    def size_up(self):
        self.size += 1
        if self.size >= 8:
            self.size = 7
            pass
        self.initialize_view(self.size)
        
    def size_down(self):
        if self.size <= 2:
            pass
        else:
            self.size -= 1
            self.initialize_view(self.size)

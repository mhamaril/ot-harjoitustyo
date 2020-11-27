from tkinter import *

from services.matrix_service import MatrixService


class MainView:
    def __init__(self, root, title):
        self.root = root
        self.title = title
        self.size = 3
        self.matrix_service = MatrixService()
        self.frame = Frame(master=self.root)
        self.matrix_a = [[]]
        self.matrix_b = [[]]
        self.matrix = [[]]
        self.result = [[]]
        self.initialize_view_matrix_3_by_3()
        
    def initialize_view_matrix_3_by_3(self):
        self.clear_view()
        self.root.title(self.title)
        matrix_a = Label(master=self.frame, text="Matrix A")
        matrix_b = Label(master=self.frame, text="Matrix B")

        matrix_a.grid(row=0, column=1)
        matrix_b.grid(row=0, column=8)

        self.a11 = Entry(master=self.frame, width=9, borderwidth=5)
        self.a11.grid(row=1, column=0)
        self.a12 = Entry(master=self.frame, width=9, borderwidth=5)
        self.a12.grid(row=1, column=1)
        self.a13 = Entry(master=self.frame, width=9, borderwidth=5)
        self.a13.grid(row=1, column=2)
        self.a21 = Entry(master=self.frame, width=9, borderwidth=5)
        self.a21.grid(row=2, column=0)
        self.a22 = Entry(master=self.frame, width=9, borderwidth=5)
        self.a22.grid(row=2, column=1)
        self.a23 = Entry(master=self.frame, width=9, borderwidth=5)
        self.a23.grid(row=2, column=2)      
        self.a31 = Entry(master=self.frame, width=9, borderwidth=5)
        self.a31.grid(row=3, column=0)
        self.a32 = Entry(master=self.frame, width=9, borderwidth=5)
        self.a32.grid(row=3, column=1)
        self.a33 = Entry(master=self.frame, width=9, borderwidth=5)
        self.a33.grid(row=3, column=2)
        self.b11 = Entry(master=self.frame, width=9, borderwidth=5)
        self.b11.grid(row=1, column=7)
        self.b12 = Entry(master=self.frame, width=9, borderwidth=5)
        self.b12.grid(row=1, column=8)
        self.b13 = Entry(master=self.frame, width=9, borderwidth=5)
        self.b13.grid(row=1, column=9)
        self.b21 = Entry(master=self.frame, width=9, borderwidth=5)
        self.b21.grid(row=2, column=7)
        self.b22 = Entry(master=self.frame, width=9, borderwidth=5)
        self.b22.grid(row=2, column=8)
        self.b23 = Entry(master=self.frame, width=9, borderwidth=5)
        self.b23.grid(row=2, column=9)
        self.b31 = Entry(master=self.frame, width=9, borderwidth=5)
        self.b31.grid(row=3, column=7)
        self.b32 = Entry(master=self.frame, width=9, borderwidth=5)
        self.b32.grid(row=3, column=8)
        self.b33 = Entry(master=self.frame, width=9, borderwidth=5)
        self.b33.grid(row=3, column=9)
       
        self.frame.grid_columnconfigure(4, minsize=100)
        self.frame.grid_columnconfigure(6, minsize=100)

        result_entry = Label(master=self.frame, text="Result")
        result_entry.grid(row=11, column=5)
        self.r11 = Entry(master=self.frame, width=9, borderwidth=5)
        self.r11.grid(row=12, column=4)
        self.r12 = Entry(master=self.frame, width=9, borderwidth=5)
        self.r12.grid(row=12, column=5)
        self.r13 = Entry(master=self.frame, width=9, borderwidth=5)
        self.r13.grid(row=12, column=6)
        self.r21 = Entry(master=self.frame, width=9, borderwidth=5)
        self.r21.grid(row=13, column=4)
        self.r22 = Entry(master=self.frame, width=9, borderwidth=5)
        self.r22.grid(row=13, column=5)
        self.r23 = Entry(master=self.frame, width=9, borderwidth=5)
        self.r23.grid(row=13, column=6)
        self.r31 = Entry(master=self.frame, width=9, borderwidth=5)
        self.r31.grid(row=14, column=4)
        self.r32 = Entry(master=self.frame, width=9, borderwidth=5)
        self.r32.grid(row=14, column=5)
        self.r33 = Entry(master=self.frame, width=9, borderwidth=5)
        self.r33.grid(row=14, column=6)

        button_inverse_a = Button(
            master=self.frame, text="Inv(A)", width=7, command=self.inverse_a)
        button_inverse_a.grid(row=6, column=1)
        button_transpose_a = Button(
            master=self.frame, text="Trans(A)", width=7, command=self.transpose_a)
        button_transpose_a.grid(row=6, column=0)
        button_determinant_a = Button(
            master=self.frame, text="Det(A)", width=7, command=self.determinant_a)
        button_determinant_a.grid(row=6, column=2)

        button_multiply_by_a = Button(
            master=self.frame, text="Multiply by", width=17, command=self.multiply_by_a)
        button_multiply_by_a.grid(row=7, column=0, columnspan=2)
        self.m_b_a = Entry(master=self.frame, width=9, borderwidth=5)
        self.m_b_a.grid(row=7, column=2)

        button_multiply_by_b = Button(
            master=self.frame, text="Multiply by", width=17, command=self.multiply_by_b)
        button_multiply_by_b.grid(row=7, column=7, columnspan=2)
        self.m_b_b = Entry(master=self.frame, width=9, borderwidth=5)
        self.m_b_b.grid(row=7, column=9)

        button_power_of_a = Button(
            master=self.frame, text="Raise to power of", width=17, command=self.power_of_a)
        button_power_of_a.grid(row=8, column=0, columnspan=2)
        self.p_o_a = Entry(master=self.frame, width=9, borderwidth=5)
        self.p_o_a.grid(row=8, column=2)

        button_power_of_b = Button(
            master=self.frame, text="Raise to power of", width=17, command=self.power_of_b)
        button_power_of_b.grid(row=8, column=7, columnspan=2)
        self.p_o_b = Entry(master=self.frame, width=9, borderwidth=5)
        self.p_o_b.grid(row=8, column=9)

        button_inverse_b = Button(
            master=self.frame, text="Inv(B)", width=7, command=self.inverse_b)
        button_inverse_b.grid(row=6, column=8)
        button_transpose_b = Button(
            master=self.frame, text="Trans(B)", width=7, command=self.transpose_b)
        button_transpose_b.grid(row=6, column=7)
        button_determinant_b = Button(
            master=self.frame, text="Det(B)", width=7, command=self.determinant_b)
        button_determinant_b.grid(row=6, column=9)

        button_axb = Button(master=self.frame, text="A x B", width=7,
                            command=self.axb)
        button_axb.grid(row=3, column=5)
        button_a_add_b = Button(master=self.frame, text="A + B",
                                width=7, command=self.a_add_b)
        button_a_add_b.grid(row=4, column=5)
        button_a_subs_b = Button(
            master=self.frame, text="A - B", width=7, command=self.a_subs_b)
        button_a_subs_b.grid(row=5, column=5)
        button_flip_matrices = Button(
            master=self.frame, text="Flip", width=7, command=self.flip_matrices)
        button_flip_matrices.grid(row=1, column=5)
        button_clear_a = Button(
            master=self.frame, text="Clear", width=7, command=self.clear_a)
        button_clear_a.grid(row=4, column=0)
        button_size_up_matrix_a = Button(master=self.frame, text="+", width=7, command=self.size_up)
        button_size_up_matrix_a.grid(row=4, column=1)
        button_size_down_matrix_a = Button(master=self.frame, text="-", width=7, command=self.size_down)
        button_size_down_matrix_a.grid(row=4, column=2)
        button_clear_b = Button(
            master=self.frame, text="Clear", width=7, command=self.clear_b)
        button_clear_b.grid(row=4, column=7)
        button_size_up_matrix_b = Button(master=self.frame, text="+", width=7, command=self.size_up)
        button_size_up_matrix_b.grid(row=4, column=8)
        button_size_down_matrix_b = Button(master=self.frame, text="-", width=7, command=self.size_down)
        button_size_down_matrix_b.grid(row=4, column=9)

        button_insert_in_a = Button(
            master=self.frame, text="Insert in A", width=17, command=self.insert_result_in_a)
        button_insert_in_a.grid(row=12, column=7, columnspan=2)
        button_insert_in_b = Button(
            master=self.frame, text="Insert in B", width=17, command=self.insert_result_in_b)
        button_insert_in_b.grid(row=13, column=7, columnspan=2)

        self.frame.pack()
    
    def initialize_view_matrix_2_by_2(self):
        self.clear_view()
        self.root.title(self.title)
        self.frame = Frame(self.root)
        matrix_a = Label(self.frame, text="Matrix A")
        matrix_b = Label(self.frame, text="Matrix B")
        
        matrix_a.grid(row=0, column=0)
        matrix_b.grid(row=0, column=7)

        self.a11 = Entry(self.frame, width=9, borderwidth=5)
        self.a11.grid(row=1, column=0)
        self.a12 = Entry(self.frame, width=9, borderwidth=5)
        self.a12.grid(row=1, column=1)
        self.a21 = Entry(self.frame, width=9, borderwidth=5)
        self.a21.grid(row=2, column=0)
        self.a22 = Entry(self.frame, width=9, borderwidth=5)
        self.a22.grid(row=2, column=1)
        self.b11 = Entry(self.frame, width=9, borderwidth=5)
        self.b11.grid(row=1, column=7)
        self.b12 = Entry(self.frame, width=9, borderwidth=5)
        self.b12.grid(row=1, column=8)
        self.b21 = Entry(self.frame, width=9, borderwidth=5)
        self.b21.grid(row=2, column=7)
        self.b22 = Entry(self.frame, width=9, borderwidth=5)
        self.b22.grid(row=2, column=8)
        
        self.frame.grid_columnconfigure(4, minsize=100)
        self.frame.grid_columnconfigure(6, minsize=100)

        result_entry = Label(self.frame, text="Result")
        result_entry.grid(row=11, column=5)
        self.r11 = Entry(self.frame, width=9, borderwidth=5)
        self.r11.grid(row=12, column=4)
        self.r12 = Entry(self.frame, width=9, borderwidth=5)
        self.r12.grid(row=12, column=5)
        self.r21 = Entry(self.frame, width=9, borderwidth=5)
        self.r21.grid(row=13, column=4)
        self.r22 = Entry(self.frame, width=9, borderwidth=5)
        self.r22.grid(row=13, column=5)
        
        button_inverse_a = Button(
            self.frame, text="Inv(A)", width=7, command=self.inverse_a)
        button_inverse_a.grid(row=6, column=1)
        button_transpose_a = Button(
            self.frame, text="Trans(A)", width=7, command=self.transpose_a)
        button_transpose_a.grid(row=6, column=0)
        button_determinant_a = Button(
            self.frame, text="Det(A)", width=7, command=self.determinant_a)
        button_determinant_a.grid(row=6, column=2)

        button_multiply_by_a = Button(
            self.frame, text="Multiply by", width=17, command=self.multiply_by_a)
        button_multiply_by_a.grid(row=7, column=0, columnspan=2)
        self.m_b_a = Entry(self.frame, width=9, borderwidth=5)
        self.m_b_a.grid(row=7, column=2)

        button_multiply_by_b = Button(
            self.frame, text="Multiply by", width=17, command=self.multiply_by_b)
        button_multiply_by_b.grid(row=7, column=7, columnspan=2)
        self.m_b_b = Entry(self.frame, width=9, borderwidth=5)
        self.m_b_b.grid(row=7, column=9)

        button_power_of_a = Button(
            self.frame, text="Raise to power of", width=17, command=self.power_of_a)
        button_power_of_a.grid(row=8, column=0, columnspan=2)
        self.p_o_a = Entry(self.frame, width=9, borderwidth=5)
        self.p_o_a.grid(row=8, column=2)

        button_power_of_b = Button(
            self.frame, text="Raise to power of", width=17, command=self.power_of_b)
        button_power_of_b.grid(row=8, column=7, columnspan=2)
        self.p_o_b = Entry(self.frame, width=9, borderwidth=5)
        self.p_o_b.grid(row=8, column=9)

        button_inverse_b = Button(
            self.frame, text="Inv(B)", width=7, command=self.inverse_b)
        button_inverse_b.grid(row=6, column=8)
        button_transpose_b = Button(
            self.frame, text="Trans(B)", width=7, command=self.transpose_b)
        button_transpose_b.grid(row=6, column=7)
        button_determinant_b = Button(
            self.frame, text="Det(B)", width=7, command=self.determinant_b)
        button_determinant_b.grid(row=6, column=9)

        button_axb = Button(self.frame, text="A x B", width=7,
                            command=self.axb)
        button_axb.grid(row=3, column=5)
        button_a_add_b = Button(self.frame, text="A + B",
                                width=7, command=self.a_add_b)
        button_a_add_b.grid(row=4, column=5)
        button_a_subs_b = Button(
            self.frame, text="A - B", width=7, command=self.a_subs_b)
        button_a_subs_b.grid(row=5, column=5)
        button_flip_matrices = Button(
            self.frame, text="Flip", width=7, command=self.flip_matrices)
        button_flip_matrices.grid(row=1, column=5)
        button_clear_a = Button(
            self.frame, text="Clear", width=7, command=self.clear_a)
        button_clear_a.grid(row=4, column=0)
        button_size_up_matrix_a = Button(self.frame, text="+", width=7, command=self.size_up)
        button_size_up_matrix_a.grid(row=4, column=1)
        button_size_down_matrix_a = Button(self.frame, text="-", width=7, command=self.size_down)
        button_size_down_matrix_a.grid(row=4, column=2)
        button_clear_b = Button(
            self.frame, text="Clear", width=7, command=self.clear_b)
        button_clear_b.grid(row=4, column=7)
        button_size_up_matrix_b = Button(self.frame, text="+", width=7, command=self.size_up)
        button_size_up_matrix_b.grid(row=4, column=8)
        button_size_down_matrix_b = Button(self.frame, text="-", width=7, command=self.size_down)
        button_size_down_matrix_b.grid(row=4, column=9)

        button_insert_in_a = Button(
            self.frame, text="Insert in A", width=17, command=self.insert_result_in_a)
        button_insert_in_a.grid(row=12, column=7, columnspan=2)
        button_insert_in_b = Button(
            self.frame, text="Insert in B", width=17, command=self.insert_result_in_b)
        button_insert_in_b.grid(row=13, column=7, columnspan=2)

        self.frame.pack()

    def transpose_a(self):
        matrix = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix)
        self.result = self.matrix_service.transpose_matrix_a()
        self.show_results(self.result)
    
    def transpose_b(self):
        matrix = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix)
        self.show_results(self.matrix_service.transpose_matrix_b())
    
    def determinant_a(self):
        matrix = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix)
        self.show_det_or_inv(self.matrix_service.determinant_matrix_a())
    
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
        self.show_results(self.matrix_service.multiply_matrix_a_by(float(self.m_b_a.get())))

    def power_of_a(self):
        matrix = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix)
        self.show_results(self.matrix_service.power_of_matrix_a(int(self.p_o_a.get())))

    def power_of_b(self):
        matrix = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix)
        self.show_results(self.matrix_service.power_of_matrix_b(int(self.p_o_b.get())))

    def multiply_by_b(self):
        matrix = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix)
        self.show_results(self.matrix_service.multiply_matrix_b_by(float(self.m_b_b.get())))
    
    def axb(self):
        matrix_a = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix_a)
        matrix_b = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix_b)
        self.show_results(self.matrix_service.a_mul_b())
    
    def a_add_b(self):
        matrix_a = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix_a)
        matrix_b = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix_b)
        self.show_results(self.matrix_service.a_plus_b())
    
    def a_subs_b(self):
        matrix_a = self.get_values_from_matrix_a()
        self.matrix_service.return_values_to_service_a(matrix_a)
        matrix_b = self.get_values_from_matrix_b()
        self.matrix_service.return_values_to_service_b(matrix_b)
        self.show_results(self.matrix_service.a_minus_b())
    
    def flip_matrices(self):
        temp_a = self.get_values_from_matrix_a()
        temp_b = self.get_values_from_matrix_b()
        self.clear_b()
        self.b11.insert(0, temp_a[0][0])
        self.b12.insert(0, temp_a[0][1])
        self.b21.insert(0, temp_a[1][0])
        self.b22.insert(0, temp_a[1][1])
        if self.size >= 3:
            self.b13.insert(0, temp_a[0][2])
            self.b23.insert(0, temp_a[1][2])
            self.b31.insert(0, temp_a[2][0])
            self.b32.insert(0, temp_a[2][1])
            self.b33.insert(0, temp_a[2][2])
        if self.size >= 4:
            self.b14.insert(0, temp_a[0][3])
            self.b24.insert(0, temp_a[1][3])
            self.b34.insert(0, temp_a[2][3])
            self.b41.insert(0, temp_a[3][0])
            self.b42.insert(0, temp_a[3][1])
            self.b43.insert(0, temp_a[3][2])
            self.b44.insert(0, temp_a[3][3])
        
        self.clear_a()
        self.a11.insert(0, temp_b[0][0])
        self.a12.insert(0, temp_b[0][1])
        self.a21.insert(0, temp_b[1][0])
        self.a22.insert(0, temp_b[1][1])
        if self.size >= 3:
            self.a13.insert(0, temp_b[0][2])
            self.a23.insert(0, temp_b[1][2])
            self.a31.insert(0, temp_b[2][0])
            self.a32.insert(0, temp_b[2][1])
            self.a33.insert(0, temp_b[2][2])
        if self.size >= 4:
            self.a14.insert(0, temp_b[0][3])
            self.a24.insert(0, temp_b[1][3])
            self.a34.insert(0, temp_b[2][3])
            self.a41.insert(0, temp_b[3][0])
            self.a42.insert(0, temp_b[3][1])
            self.a43.insert(0, temp_b[3][2])
            self.a44.insert(0, temp_b[3][3])

    def insert_result_in_a(self):
        self.clear_a()
        self.a11.insert(0, float(self.r11.get()))
        self.a12.insert(0, float(self.r12.get()))
        self.a21.insert(0, float(self.r21.get()))
        self.a22.insert(0, float(self.r22.get()))
        if self.size >= 3:
            self.a13.insert(0, float(self.r13.get()))
            self.a23.insert(0, float(self.r23.get()))
            self.a31.insert(0, float(self.r31.get()))
            self.a32.insert(0, float(self.r32.get()))
            self.a33.insert(0, float(self.r33.get()))
        if self.size >= 4:
            self.a14.insert(0, float(self.r14.get()))
            self.a24.insert(0, float(self.r24.get()))
            self.a34.insert(0, float(self.r34.get()))
            self.a41.insert(0, float(self.r41.get()))
            self.a42.insert(0, float(self.r42.get()))
            self.a43.insert(0, float(self.r43.get()))
            self.a44.insert(0, float(self.r44.get()))

    def insert_result_in_b(self):
        self.clear_b()
        self.b11.insert(0, float(self.r11.get()))
        self.b12.insert(0, float(self.r12.get()))
        self.b21.insert(0, float(self.r21.get()))
        self.b22.insert(0, float(self.r22.get()))
        if self.size >= 3:
            self.b13.insert(0, float(self.r13.get()))
            self.b23.insert(0, float(self.r23.get()))
            self.b31.insert(0, float(self.r31.get()))
            self.b32.insert(0, float(self.r32.get()))
            self.b33.insert(0, float(self.r33.get()))
        if self.size >= 4:
            self.b14.insert(0, float(self.r14.get()))
            self.b24.insert(0, float(self.r24.get()))
            self.b34.insert(0, float(self.r34.get()))
            self.b41.insert(0, float(self.r41.get()))
            self.b42.insert(0, float(self.r42.get()))
            self.b43.insert(0, float(self.r43.get()))
            self.b44.insert(0, float(self.r44.get()))

    def get_values_from_matrix_a(self):
        if self.size == 2:
            self.matrix_a = [[float(self.a11.get()), float(self.a12.get())], [float(
                self.a21.get()), float(self.a22.get())]]
        if self.size == 3:
            self.matrix_a = [[float(self.a11.get()), float(self.a12.get()), float(
                self.a13.get())], [float(self.a21.get()), float(self.a22.get()), float(
                    self.a23.get())], [float(self.a31.get()), float(self.a32.get()), float(
                        self.a33.get())]]
        if self.size == 4:
            self.matrix_a = [[float(self.a11.get()), float(self.a12.get()), float(
                self.a13.get()), float(self.a14.get())], [float(self.a21.get()), float(
                    self.a22.get()), float(self.a23.get()), float(self.a24.get())], [float(
                        self.a31.get()), float(self.a32.get()), float(self.a33.get()), float(
                            self.a34.get())],[float(self.a41.get()), float(
                                self.a42.get()), float(self.a43.get()), float(self.a44.get())]]
        else:
            pass
        return self.matrix_a

    def get_values_from_matrix_b(self):
        if self.size == 2:
            self.matrix_b = [[float(self.b11.get()), float(self.b12.get())], [float(
                self.b21.get()), float(self.b22.get())]]
        if self.size == 3:
            self.matrix_b = [[float(self.b11.get()), float(self.b12.get()), float(
                self.b13.get())], [float(self.b21.get()), float(self.b22.get()), float(
                    self.b23.get())], [float(self.b31.get()), float(self.b32.get()), float(
                        self.b33.get())]]
        if self.size == 4:
            self.matrix_b = [[float(self.b11.get()), float(self.b12.get()), float(
                self.b13.get()), float(self.b14.get())], [float(self.b21.get()), float(
                    self.b22.get()), float(self.b23.get()), float(self.b24.get())], [float(
                        self.b31.get()), float(self.b32.get()), float(self.b33.get()), float(
                            self.b34.get())],[float(self.b41.get()), float(
                                self.b42.get()), float(self.b43.get()), float(self.b44.get())]]
        else:
            pass

        return self.matrix_b

    def show_det_or_inv(self, det):
        self.reset_results()
        if type(det) == str:
            self.r12.insert(0, "      Not")
            self.r22.insert(0, "  Invertible")
        else:
            self.r22.insert(0, float(det))

    
    def show_results(self, matrix):
        self.matrix = matrix
        self.reset_results()
        self.r11.insert(0, float(self.matrix[0][0]))
        self.r12.insert(0, float(self.matrix[0][1]))
        self.r21.insert(0, float(self.matrix[1][0]))
        self.r22.insert(0, float(self.matrix[1][1]))
        if self.size >= 3:
            self.r13.insert(0, float(self.matrix[0][2]))
            self.r23.insert(0, float(self.matrix[1][2]))
            self.r31.insert(0, float(self.matrix[2][0]))
            self.r32.insert(0, float(self.matrix[2][1]))
            self.r33.insert(0, float(self.matrix[2][2]))
        if self.size >= 4:
            self.r14.insert(0, float(self.matrix[0][3]))
            self.r24.insert(0, float(self.matrix[1][3]))
            self.r34.insert(0, float(self.matrix[2][3]))
            self.r41.insert(0, float(self.matrix[3][0]))
            self.r42.insert(0, float(self.matrix[3][1]))
            self.r43.insert(0, float(self.matrix[3][2]))
            self.r44.insert(0, float(self.matrix[3][3]))
    
    def reset_results(self):
        self.r11.delete(0, END)
        self.r12.delete(0, END)
        self.r21.delete(0, END)
        self.r22.delete(0, END)
        if self.size >= 3:
            self.r13.delete(0, END)
            self.r23.delete(0, END)
            self.r31.delete(0, END)
            self.r32.delete(0, END)
            self.r33.delete(0, END)
        if self.size >= 4:
            self.r14.delete(0, END)
            self.r24.delete(0, END)
            self.r34.delete(0, END)
            self.r41.delete(0, END)
            self.r42.delete(0, END)
            self.r43.delete(0, END)
            self.r44.delete(0, END)
    
    def clear_a(self):
        self.a11.delete(0, END)
        self.a12.delete(0, END)
        self.a21.delete(0, END)
        self.a22.delete(0, END)
        if self.size >= 3:
            self.a13.delete(0, END)
            self.a23.delete(0, END)
            self.a31.delete(0, END)
            self.a32.delete(0, END)
            self.a33.delete(0, END)
        if self.size >= 4:
            self.a14.delete(0, END)
            self.a24.delete(0, END)
            self.a34.delete(0, END)
            self.a41.delete(0, END)
            self.a42.delete(0, END)
            self.a43.delete(0, END)
            self.a44.delete(0, END)

    def clear_b(self):
        self.b11.delete(0, END)
        self.b12.delete(0, END)
        self.b21.delete(0, END)
        self.b22.delete(0, END)
        if self.size >= 3:
            self.b13.delete(0, END)
            self.b23.delete(0, END)
            self.b31.delete(0, END)
            self.b32.delete(0, END)
            self.b33.delete(0, END)
        if self.size >= 4:
            self.b14.delete(0, END)
            self.b24.delete(0, END)
            self.b34.delete(0, END)
            self.b41.delete(0, END)
            self.b42.delete(0, END)
            self.b43.delete(0, END)
            self.b44.delete(0, END)
 
    def clear_view(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.pack_forget()
        
    def size_up(self):
        self.size += 1
        if self.size == 3:
            self.clear_view()
            self.initialize_view_matrix_3_by_3()
        if self.size == 4:
            self.clear_view()
            self.initialize_view_matrix_4_by_4()
        if self.size > 4:
            print("bigger sizes that 4x4 will be added later")
            pass
    
    def size_down(self):
        if self.size < 2:
            pass
        else:
            self.size -= 1
            if self.size == 2:
                self.initialize_view_matrix_2_by_2()

            if self.size == 3:
                self.initialize_view_matrix_3_by_3()

    def initialize_view_matrix_4_by_4(self):
        
        self.root.title(self.title)
        self.frame = Frame(self.root)
        matrix_a = Label(self.frame, text="Matrix A")
        matrix_b = Label(self.frame, text="Matrix B")

        matrix_a.grid(row=0, column=1)
        matrix_b.grid(row=0, column=8)

        self.a11 = Entry(self.frame, width=9, borderwidth=5)
        self.a11.grid(row=1, column=0)
        self.a12 = Entry(self.frame, width=9, borderwidth=5)
        self.a12.grid(row=1, column=1)
        self.a13 = Entry(self.frame, width=9, borderwidth=5)
        self.a13.grid(row=1, column=2)
        self.a14 = Entry(self.frame, width=9, borderwidth=5)
        self.a14.grid(row=1, column=3)
        self.a21 = Entry(self.frame, width=9, borderwidth=5)
        self.a21.grid(row=2, column=0)
        self.a22 = Entry(self.frame, width=9, borderwidth=5)
        self.a22.grid(row=2, column=1)
        self.a23 = Entry(self.frame, width=9, borderwidth=5)
        self.a23.grid(row=2, column=2)
        self.a24 = Entry(self.frame, width=9, borderwidth=5)
        self.a24.grid(row=2, column=3)  
            
        self.a31 = Entry(self.frame, width=9, borderwidth=5)
        self.a31.grid(row=3, column=0)
        self.a32 = Entry(self.frame, width=9, borderwidth=5)
        self.a32.grid(row=3, column=1)
        self.a33 = Entry(self.frame, width=9, borderwidth=5)
        self.a33.grid(row=3, column=2)
        self.a34 = Entry(self.frame, width=9, borderwidth=5)
        self.a34.grid(row=3, column=3)
        self.a41 = Entry(self.frame, width=9, borderwidth=5)
        self.a41.grid(row=4, column=0)
        self.a42 = Entry(self.frame, width=9, borderwidth=5)
        self.a42.grid(row=4, column=1)
        self.a43 = Entry(self.frame, width=9, borderwidth=5)
        self.a43.grid(row=4, column=2)
        self.a44 = Entry(self.frame, width=9, borderwidth=5)
        self.a44.grid(row=4, column=3)

        self.b11 = Entry(self.frame, width=9, borderwidth=5)
        self.b11.grid(row=1, column=8)
        self.b12 = Entry(self.frame, width=9, borderwidth=5)
        self.b12.grid(row=1, column=9)
        self.b13 = Entry(self.frame, width=9, borderwidth=5)
        self.b13.grid(row=1, column=10)
        self.b14 = Entry(self.frame, width=9, borderwidth=5)
        self.b14.grid(row=1, column=11)
        self.b21 = Entry(self.frame, width=9, borderwidth=5)
        self.b21.grid(row=2, column=8)
        self.b22 = Entry(self.frame, width=9, borderwidth=5)
        self.b22.grid(row=2, column=9)
        self.b23 = Entry(self.frame, width=9, borderwidth=5)
        self.b23.grid(row=2, column=10)
        self.b24 = Entry(self.frame, width=9, borderwidth=5)
        self.b24.grid(row=2, column=11)      
        self.b31 = Entry(self.frame, width=9, borderwidth=5)
        self.b31.grid(row=3, column=8)
        self.b32 = Entry(self.frame, width=9, borderwidth=5)
        self.b32.grid(row=3, column=9)
        self.b33 = Entry(self.frame, width=9, borderwidth=5)
        self.b33.grid(row=3, column=10)
        self.b34 = Entry(self.frame, width=9, borderwidth=5)
        self.b34.grid(row=3, column=11)
        self.b41 = Entry(self.frame, width=9, borderwidth=5)
        self.b41.grid(row=4, column=8)
        self.b42 = Entry(self.frame, width=9, borderwidth=5)
        self.b42.grid(row=4, column=9)
        self.b43 = Entry(self.frame, width=9, borderwidth=5)
        self.b43.grid(row=4, column=10)
        self.b44 = Entry(self.frame, width=9, borderwidth=5)
        self.b44.grid(row=4, column=11)
       
        self.frame.grid_columnconfigure(4, minsize=100)
        self.frame.grid_columnconfigure(6, minsize=100)

        result_entry = Label(self.frame, text="Result")
        result_entry.grid(row=11, column=5)
        self.r11 = Entry(self.frame, width=9, borderwidth=5)
        self.r11.grid(row=12, column=4)
        self.r12 = Entry(self.frame, width=9, borderwidth=5)
        self.r12.grid(row=12, column=5)
        self.r13 = Entry(self.frame, width=9, borderwidth=5)
        self.r13.grid(row=12, column=6)
        self.r14 = Entry(self.frame, width=9, borderwidth=5)
        self.r14.grid(row=12, column=7)
        self.r21 = Entry(self.frame, width=9, borderwidth=5)
        self.r21.grid(row=13, column=4)
        self.r22 = Entry(self.frame, width=9, borderwidth=5)
        self.r22.grid(row=13, column=5)
        self.r23 = Entry(self.frame, width=9, borderwidth=5)
        self.r23.grid(row=13, column=6)
        self.r24 = Entry(self.frame, width=9, borderwidth=5)
        self.r24.grid(row=13, column=7)      
        self.r31 = Entry(self.frame, width=9, borderwidth=5)
        self.r31.grid(row=14, column=4)
        self.r32 = Entry(self.frame, width=9, borderwidth=5)
        self.r32.grid(row=14, column=5)
        self.r33 = Entry(self.frame, width=9, borderwidth=5)
        self.r33.grid(row=14, column=6)
        self.r34 = Entry(self.frame, width=9, borderwidth=5)
        self.r34.grid(row=14, column=7)
        self.r41 = Entry(self.frame, width=9, borderwidth=5)
        self.r41.grid(row=15, column=4)
        self.r42 = Entry(self.frame, width=9, borderwidth=5)
        self.r42.grid(row=15, column=5)
        self.r43 = Entry(self.frame, width=9, borderwidth=5)
        self.r43.grid(row=15, column=6)
        self.r24 = Entry(self.frame, width=9, borderwidth=5)
        self.r24.grid(row=13, column=7)
        self.r34 = Entry(self.frame, width=9, borderwidth=5)
        self.r34.grid(row=14, column=7)
        self.r44 = Entry(self.frame, width=9, borderwidth=5)
        self.r44.grid(row=15, column=7)

        button_inverse_a = Button(
            self.frame, text="Inv(A)", width=7, command=self.inverse_a)
        button_inverse_a.grid(row=6, column=1)
        button_transpose_a = Button(
            self.frame, text="Trans(A)", width=7, command=self.transpose_a)
        button_transpose_a.grid(row=6, column=0)
        button_determinant_a = Button(
            self.frame, text="Det(A)", width=7, command=self.determinant_a)
        button_determinant_a.grid(row=6, column=2)

        button_multiply_by_a = Button(
            self.frame, text="Multiply by", width=17, command=self.multiply_by_a)
        button_multiply_by_a.grid(row=7, column=0, columnspan=2)
        self.m_b_a = Entry(self.frame, width=9, borderwidth=5)
        self.m_b_a.grid(row=7, column=2)

        button_multiply_by_b = Button(
            self.frame, text="Multiply by", width=17, command=self.multiply_by_b)
        button_multiply_by_b.grid(row=7, column=9, columnspan=2)
        self.m_b_b = Entry(self.frame, width=9, borderwidth=5)
        self.m_b_b.grid(row=7, column=11)

        button_power_of_a = Button(
            self.frame, text="Raise to power of", width=17, command=self.power_of_a)
        button_power_of_a.grid(row=8, column=0, columnspan=2)
        self.p_o_a = Entry(self.frame, width=9, borderwidth=5)
        self.p_o_a.grid(row=8, column=2)

        button_power_of_b = Button(
            self.frame, text="Raise to power of", width=17, command=self.power_of_b)
        button_power_of_b.grid(row=8, column=9, columnspan=2)
        self.p_o_b = Entry(self.frame, width=9, borderwidth=5)
        self.p_o_b.grid(row=8, column=11)

        button_inverse_b = Button(
            self.frame, text="Inv(B)", width=7, command=self.inverse_b)
        button_inverse_b.grid(row=6, column=10)
        button_transpose_b = Button(
            self.frame, text="Trans(B)", width=7, command=self.transpose_b)
        button_transpose_b.grid(row=6, column=9)
        button_determinant_b = Button(
            self.frame, text="Det(B)", width=7, command=self.determinant_b)
        button_determinant_b.grid(row=6, column=11)

        button_axb = Button(self.frame, text="A x B", width=7, command=self.axb)
        button_axb.grid(row=3, column=5)
        button_a_add_b = Button(self.frame, text="A + B",
                                width=7, command=self.a_add_b)
        button_a_add_b.grid(row=4, column=5)
        button_a_subs_b = Button(
            self.frame, text="A - B", width=7, command=self.a_subs_b)
        button_a_subs_b.grid(row=5, column=5)
        button_flip_matrices = Button(
            self.frame, text="Flip", width=7, command=self.flip_matrices)
        button_flip_matrices.grid(row=1, column=5)
        button_clear_a = Button(
            self.frame, text="Clear", width=7, command=self.clear_a)
        button_clear_a.grid(row=5, column=0)
        button_size_up_matrix_a = Button(self.frame, text="+", width=7, command=self.size_up)
        button_size_up_matrix_a.grid(row=5, column=1)
        button_size_down_matrix_a = Button(self.frame, text="-", width=7, command=self.size_down)
        button_size_down_matrix_a.grid(row=5, column=2)
        button_clear_b = Button(
            self.frame, text="Clear", width=7, command=self.clear_b)
        button_clear_b.grid(row=5, column=9)
        button_size_up_matrix_b = Button(self.frame, text="+", width=7, command=self.size_up)
        button_size_up_matrix_b.grid(row=5, column=10)
        button_size_down_matrix_b = Button(self.frame, text="-", width=7, command=self.size_down)
        button_size_down_matrix_b.grid(row=5, column=11)

        button_insert_in_a = Button(
            self.frame, text="Insert in A", width=17, command=self.insert_result_in_a)
        button_insert_in_a.grid(row=12, column=8, columnspan=2)
        button_insert_in_b = Button(
            self.frame, text="Insert in B", width=17, command=self.insert_result_in_b)
        button_insert_in_b.grid(row=13, column=8, columnspan=2)

        self.frame.pack()

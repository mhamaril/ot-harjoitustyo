from gui.main_view import MainView

class GUI:
    def __init__(self, root):
        self.root = root
        self.current_view = None
    
    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None

    def show_matrix_view(self):
        self.hide_current_view()
        self.current_view = MainViev(self.root, "Matric Calculator", 3)
        self.current_view.initi

    def start(self):
        self.show_matrix_view()


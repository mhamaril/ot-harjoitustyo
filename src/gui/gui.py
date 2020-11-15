from gui.main_view import MainView

class GUI:
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def show_matrix_view(self):
        self.current_view = MainViev(self.root)

    def start(self):
        self.show_matrix_view()


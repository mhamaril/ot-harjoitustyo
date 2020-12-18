from gui.login_view import LoginView
from gui.create_user_view import CreateUserView
from gui.main_view import MainView


class GUI:
    """Class responsible of graphic user interface
    """
    def __init__(self, root):
        self.root = root
        self.current_view = None

    def hide_current_view(self):
        if self.current_view:
            self.current_view.destroy()

        self.current_view = None

    def show_login_view(self):
        self.hide_current_view()
        
        self.current_view = LoginView(
            self.root,
            self.show_logged_view,
            self.show_create_user_view,
            self.show_limited_view
        )

        self.current_view.pack()

    def show_logged_view(self):
        self.hide_current_view()
        self.show_full_view()

    def show_create_user_view(self):
        self.hide_current_view()

        self.current_view = CreateUserView(
            self.root,
            self.show_logged_view,
            self.show_login_view
        )

        self.current_view.pack()

    def show_limited_view(self):
        self.hide_current_view()

        self.current_view = MainView(
            self.root,
            "Matrix Calculator --- Limited Version",
            1,
            self.show_login_view,
            self.show_login_view
        )
    def show_full_view(self):
        self.hide_current_view()

        self.current_view = MainView(
            self.root,
            "Matrix Calculator --- Full Version",
            2,
            self.show_login_view,
            self.show_login_view
        )

    def start(self):
        self.show_limited_view()

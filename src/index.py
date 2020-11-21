from tkinter import Tk
from gui.main_view import MainView
#from gui.gui import GUI

window = Tk()
window.title("Matrix Calculator")
MainView(window, "Matrix Calculator")
#ui = GUI(window)
#ui.start()

window.mainloop()

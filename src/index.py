from tkinter import Tk
from gui.gui import GUI

window = Tk()
window.title('TodoApp')

gui = GUI(window)
gui.start()

window.mainloop()

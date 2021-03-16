from tkinter import *
from tkinter import messagebox

import Student_Tracker_GUI
import Student_Tracker_func


# Creating window object for interface with Student database
class Student_Tracker(Frame):
    def __init__ (self, window):
        Frame.__init__(self)

        self.window = window
        self.window.resizable(width=True, height=True)
        self.window.geometry('{}x{}'.format(800, 500))
        self.window.config(bg='lightgray')
        Student_Tracker_func.center_window(self, 500, 500)

        self.window.title("Student Tracker")
        self.window.protocol("WM_DELETE_WINDOW", lambda: Student_Tracker_func.ask_quit(self))
        arg = self.window  

        # load GUI widgets from gui module
        Student_Tracker_GUI.load_gui(self)

        
if __name__ == "__main__":
    root = Tk()
    App = Student_Tracker(root)
    root.mainloop()
        
        

        
        
        
        


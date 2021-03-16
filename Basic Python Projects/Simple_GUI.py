import tkinter
from tkinter import *  # This way you don't have to do tkinter.<widget> for everything.


class ParentWindow(Frame):  # This will be a child class to tkinter class
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master # The main window
        self.master.resizable(width=True, height=True) # Window resizeable by user
        self.master.geometry('{}x{}'.format(700, 400))    # Size of window
        self.master.title("Learning Tkinter!")
        self.master.config(bg='lightgray')  # Set background color. Can use names.

        self.varFName = StringVar()  # How to declare string variable within tkinter
        self.varLName = StringVar()
        #self.varFName.set('Bob')     # How to assign value to variable in tkinter
        #self.varLName.set('Smith')

        self.lblFName = Label(self.master,text="First Name: ", font = ("Helvetica", 16), fg = "black", bg = "lightgray")
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0))  # Padding on left and right, top and bottom

        self.lblLName = Label(self.master,text="Last Name: ", font = ("Helvetica", 16), fg = "black", bg = "lightgray")
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))

        self.lblDisplay = Label(self.master,text="", font = ("Helvetica", 16), fg = "black", bg = "lightgray")
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        # Text box for first name with font, font size, foreground and background colors.
        self.txtFName = Entry(self.master,text=self.varFName, font = ("Helvetica", 16), fg='black', bg="lightblue")  
        self.txtFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))  # Type of managers are pack and grid

        self.txtLName = Entry(self.master,text=self.varLName, font = ("Helvetica", 16), fg='black', bg="lightblue")
        self.txtLName.grid(row=1, column=1, padx=(30,0), pady=(30,0))  # Type of placement managers are pack and grid

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit)
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky = NE)  # Sticky northeast

        self.btnCancel = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky = NE)  # Sticky northeast

    def submit(self):
        firstName = self.varFName.get()
        lastName = self.varLName.get()
        self.lblDisplay.config(text="Hello {} {}!".format(firstName, lastName))  # To change something in window while it's running, use config        

    def cancel(self):
        self.master.destroy()  # Closes window


if __name__ == "__main__":
    root = Tk()  # Calling on tkinter class 
    App = ParentWindow(root)
    root.mainloop # Keeps window open/alive
    

"""
Write a script that creates a GUI with a button widget and a text widget.
Include a function that, when it is called, will invoke a dialog modal which
will allow users the ability to select a folder directory from their system.
Finally, show the user’s selected directory path in the text field.

use the askdirectory() method from the Tkinter module.
have a function linked to the button widget so that once the button has been
clicked, the user’s selected file path will be retained by the askdirectory()
method and printed within your GUI’s text widget.
"""


from tkinter import *
from tkinter import filedialog as fd



class ParentWindow(Frame):
    def __init__(self, window):
        Frame.__init__(self)

        # Main window features
        self.window = window 
        self.window.resizable(width=True, height=True) 
        #self.window.geometry('{}x{}'.format(600, 300))    
        self.window.title("Check Files")
        self.window.config(bg='#EEE')  

        # Declare string variable within tkinter
        self.directory = StringVar()  
        self.directory2 = StringVar()

        # For assigning value to variable in tkinter
        self.directory.set('Click browse to choose a directory.')     
        self.directory2.set('')

        # Labels with font, font size, foreground and background colors, placement and padding
        #self.lblFName = Label(self.window,text="First Name: ", font = ("Helvetica", 16), fg = "black", bg = "lightgray")
        #self.lblFName.grid(row=0, column=1, padx=(30,0), pady=(30,0))  # Padding on left and right, top and bottom

        #self.lblLName = Label(self.window,text="Last Name: ", font = ("Helvetica", 16), fg = "black", bg = "lightgray")
        #self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0))  # Typically place with grid or pack

        #self.lblDisplay = Label(self.window,text="Directory: ", font = ("Helvetica", 10), fg = "black", bg = "#EEE")
        #self.lblDisplay.grid(row=2, column=0, columnspan=3, padx=(10,0), pady=(10,10), sticky = W)

        # Text boxes with font, font size, foreground and background colors, placement and padding
        #self.txtbrowse1 = Entry(self.window, text="", font = ("Helvetica", 12), fg='black', bg="#FFF", width = 30)  
        #self.txtbrowse1.grid(row=1, column=1, rowspan=1, columnspan=2, padx=(30,10), pady=(40,0), sticky = W)

        self.dirText = Text(self.window, width = 80, height = 1, font = ("Helvetica", 10), fg='black', bg="#FFF")
        self.dirText.grid(row=1, column=1, rowspan=1, columnspan=2, padx=(30,10), pady=(40,0), sticky = W)
        self.dirText.insert(1.0, '')

        
        #self.txtbrowse2 = Entry(self.master,text=self.varLName, font = ("Helvetica", 14), fg='black', bg="#FFF", width = 30)
        #self.txtbrowse2.grid(row=2, column=1, rowspan=1, columnspan=2, padx=(30,10), pady=(10,0), sticky = W)  

        # Buttons with size, command, placement and padding
        self.btnbrowse1 = Button(self.master, text="Browse...", width=12, height=1, command=self.submit)
        self.btnbrowse1.grid(row=1, column=0, padx=(20,0), pady=(40,0), sticky = NE)  # Sticky northeast
        
        #self.btnbrowse2 = Button(self.master, text="Browse...", width=12, height=1, command=self.submit)
        #self.btnbrowse2.grid(row=2, column=0, padx=(20,0), pady=(10,0), sticky = NE)  
        
        #self.btnCheck = Button(self.master, text="Check for files...", width=12, height=2, command=self.submit)
        #self.btnCheck.grid(row=3, column=0, padx=(20,0), pady=(10,10), sticky = NE)  
        
        self.btnClose = Button(self.master, text="Close Program", width=12, height=2, command=self.cancel)
        self.btnClose.grid(row=3, column=2, padx=(0,10), pady=(10,10), sticky = NE)  

    def submit(self):
        """ invoke a dialog modal which will allow users the ability to select a folder directory from their system """
        self.directory = fd.askdirectory()
        
        self.dirText.insert(1.0, "{}".format(self.directory))  # To change something in window while it's running, use config        
        
        #self.lblDisplay.config(text="Directory: {}".format(self.directory))  # To change something in window while it's running, use config        
        

    def cancel(self):
        self.master.destroy()  # Closes window
        
        
        




if __name__ == "__main__":
    root = Tk()
    mainWindow = ParentWindow(root)
    root.mainloop


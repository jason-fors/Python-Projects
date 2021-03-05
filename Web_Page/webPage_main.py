from tkinter import *
import webPage_functions


class ParentWindow(Frame):
    def __init__(self, window):
        Frame.__init__(self)

        # Main window features
        self.window = window 
        self.window.resizable(width=True, height=True) 
        self.window.title("Web Page Editor")
        self.window.config(bg='#EEE')  

        # Declare string variable within tkinter
        # self.varWebPageBody = StringVar()  

        # For assigning value to variable in tkinter
        # self.varWebPageBody.set('')     

        # Labels with font, font size, foreground and background colors, placement and padding
        self.lblFName = Label(self.window,text="Existing Content: ", font = ("Helvetica", 16), fg = "black", bg = "#EEE")
        self.lblFName.grid(row=0, column=0, padx=(30,0), pady=(30,0), sticky=NW)  

        self.lblLName = Label(self.window,text="New Content: ", font = ("Helvetica", 16), fg = "black", bg = "#EEE")
        self.lblLName.grid(row=1, column=0, padx=(30,0), pady=(30,0), sticky=NW)  

        self.lblDisplay = Label(self.window,text="", font = ("Helvetica", 16), fg = "black", bg = "#EEE")
        self.lblDisplay.grid(row=3, column=1, padx=(30,0), pady=(30,0))

        # Text boxes with font, font size, foreground and background colors, placement and padding
        self.curText = Text(self.window, width = 80, height = 5, font = ("Helvetica", 10), fg='black', bg="#FFF")
        self.curText.grid(row=0, column=1, rowspan=1, columnspan=2, padx=(30,10), pady=(30,0), sticky = W)
        self.curText.insert(1.0, textContent)

        self.newText = Text(self.window, width = 80, height = 5, font = ("Helvetica", 10), fg='black', bg="#FFF")
        self.newText.grid(row=1, column=1, rowspan=1, columnspan=2, padx=(30,10), pady=(30,0), sticky = W)
        self.newText.insert(1.0, 'Enter new content here.')

        # Buttons with size, command, placement and padding
        self.btnGet = Button(self.window, text="Get Current Content", width=20, height=2, command=self.displayContent)
        self.btnGet.grid(row=0, column=10, padx=(10,10), pady=(30,0), sticky = NE)  # Sticky northeast

        self.btnChange = Button(self.window, text="Submit New Content", width=20, height=2, command=self.submitContent)
        self.btnChange.grid(row=1, column=10, padx=(10,10), pady=(30,0), sticky = NE)  # Sticky northeast

        self.btnBrowser = Button(self.window, text="Show Page", width=10, height=2, command=self.showPage)
        self.btnBrowser.grid(row=2, column=1, padx=(50,0), pady=(30,0), sticky = NW)  

        self.btnCancel = Button(self.window, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnCancel.grid(row=2, column=1, padx=(0,50), pady=(30,0), sticky = NE)  

    def displayContent(self):
        """ gets current content from web page body """
        pageContent = webPage_functions.getBody("pyWebPage.html")
        self.curText.delete(1.0,END)                        # Emptying text box before inserting new content.
        self.curText.insert(1.0, "{}".format(pageContent))  # Inserting web page body text to text box.

    def submitContent(self):
        """ updates content in web page body with text in text box """
        newContent = self.newText.get(1.0,END)              # Putting user entry into text box in a variable.
        webPage_functions.writeBody("pyWebPage.html", newContent)  # Write new content to file.

    def showPage(self):
        """ loads web page in browser """
        webPage_functions.openPage("pyWebPage.html")

    def cancel(self):
        self.master.destroy()  # Closes window




if __name__ == "__main__":
    webPage_functions.makeWebPage("pyWebPage.html")
    textContent = webPage_functions.getBody("pyWebPage.html")
    root = Tk()
    mainWindow = ParentWindow(root)
    root.mainloop


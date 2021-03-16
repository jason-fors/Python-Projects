import os
from tkinter import *
import sqlite3

import Student_Tracker_Main
import Student_Tracker_GUI


def center_window(self, w, h):
    """ centers window in user's screen """
    screen_width = self.window.winfo_screenwidth()
    screen_height = self.window.winfo_screenheight()
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.window.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo


# Catch user click of 'X' to close window
def ask_quit(self):
    if messagebox.askokcancel("Exit program", "Okay to exit application?"):
        # close app
        self.window.destroy()
        os._exit(0)


def create_db(self):
    """ Creates student tracker database """
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            students_fname TEXT, \
            students_lname TEXT, \
            students_fullname TEXT, \
            students_phone TEXT, \
            students_email TEXT, \
            students_course TEXT);")
        conn.commit()
    conn.close()
    first_run(self)


def first_run(self):
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("INSERT INTO tbl_students (students_fname, students_lname, students_fullname, students_phone, students_email, students_course) VALUES (?,?,?,?,?,?)", ('John','Doe','John Doe','111-111-1111','jdoe@email.com', 'Orientation'))
            conn.commit()
    conn.close()


def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM tbl_students""")
    count = cur.fetchone()[0]
    return cur,count


#Select item in ListBox
def onSelect(self, event):
    # calling the event is the self.lstList1 widget
    varList = event.widget
    select = varList.curselection()[0]  #comes as a tuple
    value = varList.get(select)
    conn = sqlite3.connect('db_students.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT students_fname, students_lname, students_phone, students_email, students_course FROM tbl_students WHERE students_fullname = (?)", [value])
        varBody = cursor.fetchall()  # Returns a tuple
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_course.delete(0,END)
            self.txt_course.insert(0,data[4])

def addToList(self):
    var_fname = self.txt_fname.get()
    var_lname = self.txt_lname.get()
    var_fname = var_fname.strip() # cleaning up user's entry
    var_lname = var_lname.strip()
    var_fname = var_fname.title() # Title case
    var_lname = var_lname.title()
    var_fullname = ("{} {}".format(var_fname,var_lname))
    var_phone = self.txt_phone.get().strip()
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if not "@" or not "." in var_email:
        print("Incorrect email format!")
    if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email)>0) and (len(var_course)>0):
        conn = sqlite3.connect('db_students.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("SELECT COUNT(students_fullname) FROM tbl_students WHERE students_fullname = '{}'".format(var_fullname))
            count = cursor.fetchone()[0]
            chkName = count
            if chkName == 0:  # fullname not present and can be added
                cursor.execute("INSERT INTO tbl_students (students_fname, students_lname, students_fullname, \
                    students_phone, students_email, students_course) \
                    VALUES (?,?,?,?,?,?)", (var_fname, var_lname, var_fullname, var_phone, var_email, var_course))
                self.lstList1.insert(END, var_fullname) # update listbox with new fullname
                onClear(self) # clear textboxes
            else:
                messagebox.showerror("Name Error", "'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                onClear(self)
        conn.commit()
        conn.close()
    else:
        messagebox.showerror("Missing Text Error","Please ensure that there is data in all five fields.")
                           

def onDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) # Listbox's selected value
    conn = sqlite3.connect('db_students.db')
    with conn:
        cur = conn.cursor()
        # check count to ensure that this is not the last record in
        # the database...cannot delete last record or we will get an error
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        if count > 1:
            confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
            if confirm:
                conn = sqlite3.connect('db_students.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM tbl_students WHERE students_fullname = '{}'""".format(var_select))
                onDeleted(self) # call the function to clear all of the textboxes and the selected index of listbox
                conn.commit()
        else:
            confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
    conn.close()


def onDeleted(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def onClear(self):
    # clear the text in these textboxes
    self.txt_fname.delete(0,END)
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)
    self.txt_course.delete(0,END)


def onRefresh(self):
    # Populate the listbox, coinciding with the database
    self.lstList1.delete(0,END)
    conn = sqlite3.connect('db_students.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
                cursor.execute("""SELECT students_fullname FROM tbl_students""")
                varList = cursor.fetchall()[i]
                for item in varList:
                    self.lstList1.insert(0,str(item))
                    i = i + 1
    conn.close()
    

                    
def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] # index of the list selection
        var_value = self.lstList1.get(var_select) # list selection's text value
    except:
        messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
        return
    # The user will only be alowed to update changes for phone, email, and course.
    # For name changes, the user will need to delete the entire record and start over.
    var_phone = self.txt_phone.get().strip() # normalize the data to maintain database integrity
    var_email = self.txt_email.get().strip()
    var_course = self.txt_course.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0): # ensure that there is data present
        conn = sqlite3.connect('db_students.db')
        with conn:
            cur = conn.cursor()
            # count records to see if the user's changes are already in
            # the database...meaning, there are no changes to update.
            cur.execute("""SELECT COUNT(students_phone) FROM tbl_students WHERE students_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count)
            cur.execute("""SELECT COUNT(students_email) FROM tbl_students WHERE students_email = '{}'""".format(var_email))
            count2 = cur.fetchone()[0]
            print(count2)
            cur.execute("""SELECT COUNT(students_course) FROM tbl_students WHERE students_course = '{}'""".format(var_course))
            count3 = cur.fetchone()[0]
            print(count3)            
            if count == 0 or count2 == 0 or count3 == 0: # if proposed changes are not already in the database, then proceed
                response = messagebox.askokcancel("Update Request","The following changes ({}), ({}) and ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_phone,var_email,var_course, var_value))
                print(response)
                if response:
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_students SET students_phone = '{0}',students_email = '{1}', students_course = '{2}' WHERE students_fullname = '{3}'""".format(var_phone,var_email,var_course,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
            else:
                messagebox.showinfo("No changes detected","All of ({}), ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone, var_email, var_course))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone, email or course information.")
    onClear(self)


if __name__ == "__main__":
    pass



    

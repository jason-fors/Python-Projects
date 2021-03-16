from tkinter import *

import Student_Tracker_Main
import Student_Tracker_func


def load_gui(self):
    """ Define tkinter widgets and configuration, and place them. """
    self.lbl_fname = Label(self.window,text='First Name:')
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_lname = Label(self.window,text='Last Name:')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_phone = Label(self.window,text='Phone Number:')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_email = Label(self.window,text='Email Address:')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    self.lbl_course = Label(self.window,text='Current course:')
    self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.txt_fname = Entry(self.window,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_lname = Entry(self.window,text='')
    self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_phone = Entry(self.window,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_email = Entry(self.window,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
    self.txt_course = Entry(self.window,text='')
    self.txt_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #Define the listbox with a scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.window,orient=VERTICAL)
    self.lstList1 = Listbox(self.window,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: Student_Tracker_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=7,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=7,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)
    
    self.btn_add = Button(self.window,width=12,height=2,text='Add',command=lambda: Student_Tracker_func.addToList(self))
    self.btn_add.grid(row=10,column=0,padx=(25,0),pady=(45,10),sticky=W)
    self.btn_update = Button(self.window,width=12,height=2,text='Update',command=lambda: Student_Tracker_func.onUpdate(self))
    self.btn_update.grid(row=10,column=1,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_delete = Button(self.window,width=12,height=2,text='Delete',command=lambda: Student_Tracker_func.onDelete(self))
    self.btn_delete.grid(row=10,column=2,padx=(15,0),pady=(45,10),sticky=W)
    self.btn_close = Button(self.window,width=12,height=2,text='Close',command=lambda: Student_Tracker_func.ask_quit(self))
    self.btn_close.grid(row=10,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

    Student_Tracker_func.create_db(self)
    Student_Tracker_func.onRefresh(self)


if __name__ == "__main__":
    pass

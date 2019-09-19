from tkinter import *
from tkinter import Tk
from tkinter import filedialog
import os

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width= False, height= False)
        self.master.geometry('{}x{}'.format(415, 200))
        self.master.title('Check Files')
        self.master.config(bg='lightgray')

        self.varInputFile = StringVar()

        self.lblFile = Label(self.master, text='File: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblFile.grid(row=0, column=0, padx=(30, 0), pady=(30, 0))

        self.txtInputTop = Entry(self.master,text = self.varInputFile, font=("Helvetica", 12), fg ='black', bg= 'white' )
        self.txtInputTop.grid(row =0 ,column = 1, padx =(30,0), pady=(50,0), columnspan=6 )

        self.btnCheckFiles = Button(self.master, text = "Browse Files...", width= 13, height = 2, command = self.Browse)
        self.btnCheckFiles.grid(row =2 ,column = 0, padx =(20,0), pady=(10,0), sticky= S+W)

        self.btnclose = Button(self.master, text="Cancel", width=14, height=2, command = self.close)
        self.btnclose.grid(row=2, column=6, padx=(0,0), pady=(10,0), sticky=E)

    def close(self):
        self.master.destroy()

    def Browse (self):
        dir= filedialog.askdirectory()
        self.varInputFile.set(dir)
        print(dir)

if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
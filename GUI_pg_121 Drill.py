from tkinter import *

class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)

        self.master = master
        self.master.resizable(width= False, height= False)
        self.master.geometry('{}x{}'.format(415, 200))
        self.master.title('Check Files')
        self.master.config(bg='lightgray')

        self.varInputTop = StringVar()
        self.varInputBtm = StringVar()

        self.txtInputTop =  Entry(self.master,text = self.varInputTop, font=("Helvetica", 16), fg ='black', bg= 'white' )
        self.txtInputTop.grid(row =0 ,column = 1, padx =(30,0), pady=(50,0), columnspan=6)

        self.txtInputBtm = Entry(self.master, text=self.varInputBtm, font=("Helvetica", 16), fg='black', bg='white')
        self.txtInputBtm.grid(row =1 ,column = 1, padx =(30,0), pady=(10,0), columnspan=6)
## Buttons+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.btnBrowseTop = Button(self.master, text="Browse...", width=13, height=1)
        self.btnBrowseTop.grid(row=0, column=0, padx=(20, 0), pady=(50, 0), sticky=W)

        self.btnBrowseBtm = Button(self.master, text="Browse...", width=13, height=1)
        self.btnBrowseBtm.grid(row=1, column=0, padx=(20, 0), pady=(10, 0), sticky=W)

        self.btnCheckFiles = Button(self.master, text = "Check For Files...", width= 13, height = 2)
        self.btnCheckFiles.grid(row =2 ,column = 0, padx =(20,0), pady=(10,0), sticky= S+W)

        self.btnclose = Button(self.master, text="Close Program", width=14, height=2, command = self.close)
        self.btnclose.grid(row=2, column=6, padx=(0,0), pady=(10,0), sticky=E)

    def close(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    app = ParentWindow(root)
    root.mainloop()
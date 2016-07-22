#from tkinter import *
#from tkinter import ttk

import tkinter as tk
from tkinter.filedialog import askopenfilename,asksaveasfilename
from imagedatahider import ImageDataHider

class HideDataApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.wm_title("Data Hider")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (StartPage, HidePage, ExtractPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self,cont):
        
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page")
        label.grid(column=0, row=0, pady=10, padx=10)

        hideBtn = tk.Button(self, text="Hide Data", 
                command=lambda: controller.show_frame(HidePage))
        hideBtn.grid(column=0, row=1)
        
        extractBtn = tk.Button(self, text="Extract Data", 
                command=lambda: controller.show_frame(ExtractPage))
        extractBtn.grid(column=1,row=1)


class HidePage(tk.Frame):

    def __init__(self,parent,controller):

        self.keyFile=""
        self.dataFile=""

        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Hide Page")
        label.grid(column=0, row=0, pady=10, padx=10)
        
        # Made keyLabel and dataLabel a class variables since we need to change their text
        self.keyLabel = tk.Label(self, text="Key File: ")
        self.keyLabel.grid(column=0, row=1)

        keyBtn = tk.Button(self, text="Open", command=self.load_key_file,width=10)
        keyBtn.grid(column=1, row=1)

        self.dataLabel = tk.Label(self, text="Data File: ")
        self.dataLabel.grid(column=0, row=2)

        dataBtn = tk.Button(self, text="Open", command=self.load_data_file,width=10)
        dataBtn.grid(column=1, row=2)
        
        backBtn = tk.Button(self, text="Back", 
                command=lambda: controller.show_frame(StartPage))

        backBtn.grid(column=0, row=5)

        hideBtn = tk.Button(self, text="Hide", command=self.hide_file)
        hideBtn.grid(column=1, row=5)

    def load_key_file(self):
        fname = askopenfilename(filetypes=[("Image Files","*.png")])

        if fname:
            try:
                self.keyFile = fname
                self.keyLabel.config(text="Key File: %s" %fname)
            except:
                print("Could not open file %s" %fname)

    def load_data_file(self):
        fname = askopenfilename()

        if fname:
            try:
                self.dataFile = fname
                self.dataLabel.config(text="Data File: %s" %fname)
            except:
                print("Could not open file %s" %fname)

    def hide_file(self):
        idh = ImageDataHider()
        idh.keyFName = self.keyFile
        idh.dataFName = self.dataFile
        idh.cipherOutFName = asksaveasfilename(filetypes=[("Image Files","*.png")]) 
        idh.hide()

class ExtractPage(tk.Frame):

    def __init__(self,parent,controller):
        
        self.keyFile = ""
        self.cipherFile = ""
        
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Extract Page")
        label.grid(column=0, row=0)

        # Made keyLabel and dataLabel a class variables since we need to change their text
        self.keyLabel = tk.Label(self, text="Key File: ")
        self.keyLabel.grid(column=0, row=1)

        keyBtn = tk.Button(self, text="Open", command=self.load_key_file,width=10)
        keyBtn.grid(column=1, row=1)

        self.cipherLabel = tk.Label(self, text="Cipher File: ")
        self.cipherLabel.grid(column=0, row=2)

        cipherBtn = tk.Button(self, text="Open", command=self.load_cipher_file,width=10)
        cipherBtn.grid(column=1, row=2)
        
        backBtn = tk.Button(self, text="Back", 
                command=lambda: controller.show_frame(StartPage))

        backBtn.grid(column=0, row=3)


        extractBtn = tk.Button(self, text="Extract", command=self.extract_file,width=10)

        extractBtn.grid(column=1, row=3)


    def load_key_file(self):
        fname = askopenfilename(filetypes=[("Image Files","*.png")])

        if fname:
            try:
                self.keyFile = fname
                self.keyLabel.config(text="Key File: %s" %fname)
            except:
                print("Could not open file %s" %fname)


    def load_cipher_file(self):
        fname = askopenfilename(filetypes=[("Image Files","*.png")])

        if fname:
            try:
                self.cipherFile = fname
                self.cipherLabel.config(text="Key File: %s" %fname)
            except:
                print("Could not open file %s" %fname)

    def extract_file(self):
        idh = ImageDataHider()
        idh.keyFName = self.keyFile
        idh.cipherFName = self.cipherFile
        idh.cipherOutFName = asksaveasfilename()
        idh.extract()


if __name__ == '__main__':
    main = HideDataApp()
    main.mainloop()

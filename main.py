from Tkinter import *
from tkFileDialog import askopenfilename
import tkMessageBox
import tkFont
import re

#notes by Giovanni Rescigno
#GPL 2.0 Clone computers free software
class notebook:
    
    def __init__(self):#opens the file
        self.filename = "notebook.txt"
        try:
            self.mainFile = open(self.filename, "r+")
            #print "file", self.mainFile.name,"opened notebook.__init__"
        except:
            
            #print "ERROR notebook file not found" # if the file is not opened an error will apperar 
            return "error: file not found"
        
        self.readnote()
        self.mainFile.close()
        
    def readnote(self): #reads the file
        
        self.maintext = self.mainFile.read()
        self.maintext = re.split("<note>", self.maintext)# if the the tag "<note>" is found than the file is split
        
        #print "adding file", self.mainFile.name 
        ##print self.maintext

        for self.text in self.maintext:#reads the text document
            if self.text != self.maintext[0]:
                Gui.listbox.insert(END, self.text[0:12])#puts i into the list box
            
        Gui.mainEntrynote.insert(END, self.maintext[0])#puts i in to the text document
        
        
    def refresh(self):
        ##print self.maintext
        self.filewright = open(self.filename, "r+")
        self.run = 0
        for self.textlist in self.maintext:
            if self.run == 1:#make shre that the 1st index dose not get inclueded
                self.filewright.write("<note>" + self.textlist) #wrights to the text document
            self.run = 1
           
        
        self.filewright.close()
        self.mainFile = open(self.filename, "r+")
        Gui.listbox.delete(0, END)
        
    def remove(self):
        
        self.filewright = open(self.filename, "wb")
        self.run = 0
        for self.textlist in self.maintext:
            #print self.textlist
            if self.run == 1:
                self.filewright.write("<note>" + self.textlist)
            self.run = 1
        
        self.filewright.close()
        self.mainFile = open(self.filename, "r+")
        Gui.listbox.delete(0, END) 
        
    def changefile(self, filename):
        
        self.filename = filename
        try:
            self.mainFile = open(self.filename, "r+")
            #print "file", self.mainFile.name,"opened notebook.__init__"
        except:
            
            #print "ERROR notebook file not found" # if the file is not opened an error will apperar 
            #tkMessageBox.showinfo("ERROR", "that file dose not exist")
            return "error: file not found"
        
        Gui.listbox.delete(0, END) 
        self.readnote()
        self.mainFile.close()
        
        
               
        
class main:

    def __init__(self):
        
        
        self.listframe = Frame(root, height=400, width=250, bg = 'white')
        self.addframe = Frame(root, height=400, width=400, bg = "white")
        self.menuframe = Frame(root, height=20, width=400, bg = "white")
        
        self.menuframe.pack(side=TOP, fill=X)
        self.listframe.pack(side=LEFT, padx=5)
        self.addframe.pack(side=LEFT, fill=Y)
        
        self.customFont = tkFont.Font(family="verdana", size=12)
        
        menubar = Menu(root)
        filemenu = Menu(menubar, tearoff=1)
        filemenu.add_command(label="Save", command=self.addnotetolist)
        filemenu.add_command(label="Open", command=self.openNewFile)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        notemenu = Menu(menubar, tearoff=0)
        notemenu.add_command(label="about", command=self.about)
        menubar.add_cascade(label="notbook", menu=notemenu)
         

        # display the menu
        root.config(menu=menubar)
        
        self.listnote(self.listframe)
        self.addnote(self.addframe)
        

    def listnote(self, master): #add the selcter and button controles

        self.spacer = Frame(master, height = 0)
        self.spacer.grid(row=0, column=0)
        
        self.notelist = Frame(master)
        self.notelist.grid(row=1, column=0)
        
        self.listbox = Listbox(self.notelist, height=24)
        self.scroller = Scrollbar(self.notelist)

        self.listbox.pack(side=LEFT, fill=Y)
        self.scroller.pack(side=LEFT, fill=Y)

        self.listbox.configure(yscrollcommand = self.scroller.set)
        self.scroller.configure(command = self.listbox.yview)
        
        self.listbox.bind('<<ListboxSelect>>', self.listhandler)
        
        ###controls##
    
        self.buttonbox = Frame(master)
        self.buttonbox.grid(row=2, column=0, sticky=W, padx=2)
        
        self.add = Button(self.buttonbox,height=1 ,width=1 ,text="+", command = self.createNewNote)
        self.distroy = Button(self.buttonbox, height=1, width=1 ,text="-", command=self.delete)

        self.add.pack(side=LEFT)
        self.distroy.pack(side=LEFT)

    def addnote(self, master):
        
        self.topframe = Frame(master)
        self.topframe.pack(side = TOP, padx=50, pady=2)

        self.midframe = Frame(master)
        self.midframe.pack(side=TOP, fill=Y, padx=5)
        
        self.mainEntrynote = Text(self.midframe, cursor="ibeam"
                                   , width=45, height=27, font=self.customFont)
        self.mainEntrynote.pack(side=LEFT)
        
        self.textscr = Scrollbar(self.midframe)
        self.textscr.pack(side=LEFT, fill=Y)
        
        self.textscr.config(command=self.mainEntrynote.yview)
        self.mainEntrynote.config(yscrollcommand=self.textscr.set)
        
        self.bottomframe = Frame(master)
        self.bottomframe.pack(side=TOP, fill = X)
        
    def listhandler(self, event):#if the list box is clicked
        
        #print notebook.maintext
        self.lisboxliss = event.widget #find the index of that list box
        self.index = int(self.lisboxliss.curselection()[0])
        Gui.mainEntrynote.delete(1.0, END) 
        Gui.mainEntrynote.insert(END, notebook.maintext[self.index+1]) #corasponds to a index on a list
        
    def createNewNote(self):#opens a new note
        
        self.mainEntrynote.delete(1.0, END)
        self.mainEntrynote.insert(END, "your notes here!")
        
    def addnotetolist(self): #adds note to the list
        
        self.newnote = self.mainEntrynote.get(1.0, END)#geting the test form the entry
        notebook.maintext.append(self.newnote)#appends it to the list of notes
        
        notebook.refresh()#runs the refresh which adds the note to the file
        notebook.readnote()#open the note back up    
        
    def delete(self):
        
        #print self.index+1
        del notebook.maintext[self.index+1]
        #print notebook.maintext
        self.listbox.delete(self.index, self.index)
        
        notebook.remove()
        notebook.readnote()
        
    def about(self):
        
        self.about = Toplevel()
        self.about.title("notebook")
        self.about.geometry("200x100")
        
        #self.photo = PhotoImage(file="notebook.gif")
        self.name = Label(self.about, text="clone notebook")
        self.name.pack(side="top")
        self.subtitle = Label(self.about, text="developed by Clone Computers")
        self.subtitle.pack(side = "top")
        
    def openNewFile(self):
        
        self.nameOfFile = askopenfilename() 
        print self.nameOfFile
        notebook.changefile(self.nameOfFile)
        
        
    def cangefile(self):
        
        notebook.changefile(self.textfile.get())
        self.window.destroy()

    
root = Tk()
root.title("notebook")
root.resizable(FALSE,FALSE)

Gui = main() 
notebook = notebook()

root.mainloop()
      


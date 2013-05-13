from Tkinter import *
import re

#notes by Giovanni Rescigno
#GPL 2.0 Clone computers free software
#articals http://www.tkdocs.com/tutorial/text.html
#http://docs.python.org/2/library/sqlite3.html
class notebook:
    
    def __init__(self):#opens the file
        try:
            self.mainFile = open("notebook.txt", "r+")
            print "file", self.mainFile.name,"opened notebook.__init__"
        except:
            
            print "ERROR notebook file not found" # if the file is not opened an error will apperar 
            return "error"
        
        self.readnote()
        self.mainFile.close()
        
    def readnote(self): #reads the file
        
        self.maintext = self.mainFile.read()
        self.maintext = re.split("<note>", self.maintext)# if the the tag "<note>" is found than the file is split
        
        print "adding file", self.mainFile.name 
        #print self.maintext
        
        for self.text in self.maintext:
             
            Gui.listbox.insert(END, self.text[0:12])
        
        Gui.mainEntrynote.insert(END, self.maintext[0])
            
    def addnote(self):
        
        print "notebook.addnote clicked"
        self.newnote = Gui.mainEntrynote.get(1.0, END)
        self.maintext.append(self.newnote)
        
        self.refresh()
        
        
    def refresh(self):
        
        for self.textlist in self.maintext:
            
            self.filewright = open("notebook.txt", "wb+")
            self.file.wright("<note>" + self.textlist)
            
        Gui.listbox.delete(0, END)
        self.filewright.close()
        self.readnote()
        
        
class main:

    def __init__(self):
        

        self.listframe = Frame(root, height=400, width=250, bg = 'white')
        self.addframe = Frame(root, height=400, width=400, bg = "white")
        
        self.listframe.pack(side=LEFT, padx=5)
        self.addframe.pack(side=LEFT, fill=Y)
        #self.label3.grid(columnspan=2, row=1, column=0)

        self.listnote(self.listframe)
        self.addnote(self.addframe)

    def listnote(self, master): #add the selcter and button controles

        self.spacer = Frame(master, height = 15)
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
        self.distroy = Button(self.buttonbox, height=1, width=1 ,text="-")

        self.add.pack(side=LEFT)
        self.distroy.pack(side=LEFT)

    def addnote(self, master):

        self.topframe = Frame(master)
        self.topframe.pack(side = TOP, padx=50, pady=8)

        self.midframe = Frame(master)
        self.midframe.pack(side=TOP, fill=Y, padx=5)
        
        self.mainEntrynote = Text(self.midframe, cursor="ibeam"
                                   , width=45, height=27)
        self.mainEntrynote.pack(side=LEFT)
        
        self.textscr = Scrollbar(self.midframe)
        self.textscr.pack(side=LEFT, fill=Y)
        
        self.textscr.config(command=self.mainEntrynote.yview)
        self.mainEntrynote.config(yscrollcommand=self.textscr.set)
        
        self.bottomframe = Frame(master)
        self.bottomframe.pack(side=TOP, fill = X)
        
        self.save = Button(self.bottomframe, text="save", command=notebook.addnote)
        self.save.pack(side = RIGHT, padx = 5)
        
    def listhandler(self, event):
        
        self.lisboxliss = event.widget
        self.index = int(self.lisboxliss.curselection()[0])
        Gui.mainEntrynote.delete(1.0, END) 
        Gui.mainEntrynote.insert(END, notebook.maintext[self.index]) 
        
    def createNewNote(self):
        
        self.mainEntrynote.delete(1.0, END)
        self.mainEntrynote.insert(END, "your notes here!")
        
    
        
root = Tk()
root.title("note book")
root.resizable(FALSE,FALSE)

Gui = main() 
notebook = notebook()

root.mainloop()
      


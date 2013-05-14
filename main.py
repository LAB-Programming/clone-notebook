from Tkinter import *
import tkFont
import re

#notes by Giovanni Rescigno
#GPL 2.0 Clone computers free software

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

        for self.text in self.maintext:#reads the text document
            if self.text != self.maintext[0]:
                Gui.listbox.insert(END, self.text[0:12])#puts i into the list box
            
        Gui.mainEntrynote.insert(END, self.maintext[0])#puts i in to the text document
        
        
    def refresh(self):
        print self.maintext
        self.filewright = open("notebook.txt", "r+")
        self.run = 0
        for self.textlist in self.maintext:
            if self.run == 1:#make shre that the 1st index dose not get inclueded
                self.filewright.write("<note>" + self.textlist) #wrights to the text document
            self.run = 1
           
        
        self.filewright.close()
        self.mainFile = open("notebook.txt", "r+")
        Gui.listbox.delete(0, END)
        
        
        
class main:

    def __init__(self):
        
        
        self.listframe = Frame(root, height=400, width=250, bg = 'white')
        self.addframe = Frame(root, height=400, width=400, bg = "white")
        self.menuframe = Frame(root, height=20, width=400, bg = "white")
        
        self.menuframe.pack(side=TOP, fill=X)
        self.listframe.pack(side=LEFT, padx=5)
        self.addframe.pack(side=LEFT, fill=Y)
        
        self.customFont = tkFont.Font(family="verdana", size=12)
        
        self.menu(self.menuframe)
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
        self.distroy = Button(self.buttonbox, height=1, width=1 ,text="-")

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
        
        self.save = Button(self.bottomframe, text="save", command=self.addnotetolist)
        self.save.pack(side = RIGHT, padx = 5)
        
    def listhandler(self, event):#if the list box is clicked
        
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
        
        return None
    
    def menu(self, master):
        
        self.master = master
        self.menubar = Menu(self.master)
        
        self.fileMenu = Menu(self.menubar)
        self.menubar.add_cascade(label="File", menu=self.fileMenu)
        self.fileMenu.add_command(label="save")
        
        
        root.config(menu=self.menubar)
        
        
    
        
    
        
root = Tk()
root.title("notebook")
root.resizable(FALSE,FALSE)

Gui = main() 
notebook = notebook()

root.mainloop()
      


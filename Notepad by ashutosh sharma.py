from tkinter import *
from tkinter.messagebox import _show
from tkinter.filedialog import asksaveasfile,askopenfile

root=Tk()
root.geometry("580x505")
file=None
sc=StringVar()
sc.set("")

def About():
    _show("Notepad by Ashutosh Sharma","This notepad is coded by ashutosh sharma "
                                       "this notepad is prepared by the help of tkinter module in python programming  "
                                       "Contact us:- gmail id  Mr.luckysharma7@gmail.com "
          )

def savefile():
    global file
    if file==None:
        file=asksaveasfile(initialfile="untited.txt",defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
        if file=="":
            showerror("Notepad","file is empty,unable to save")
            file=None
        else:
            file.write(t.get(1.0,END))
            file.close()
def newfile():
    global file
    root.title("untited Notepad")
    file=None
    t.delete(1.0,END)

def openfile():
    global  file
    file=askopenfile(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Document","*.txt")])
    if file=="":
        file=None
    else:
        t.delete(1.0,END)
        #f=open(file,"r")
        t.insert(1.0,file.read())
        file.close()

def Quit():
    root.destroy()

def cut():
    t.event_generate(("<<Cut>>"))
def Copy():
    t.event_generate(("<<Copy>>"))
def Paste():
    t.event_generate(("<<Paste>>"))

def font():
    ashu=Toplevel(root)
    def z():
        ashu.destroy()

    def font_changer():
        font1=l1.curselection()
        size=l2.curselection()
        style=l3.curselection()
        p = (l1.get(font1), l2.get(size), l3.get(style))
        t.configure(font=p)

        ashu.destroy()
    ashu.title("Font")

    Label(ashu,text="Select your desires font",font="llucida 20 bold").pack()

    Button(ashu, text="Cancel", command=z).pack(side=BOTTOM,padx=10,anchor="se")
    Button(ashu, text="Ok", command=font_changer).pack(side=BOTTOM,padx=10,ipadx=10,anchor="se")

    l1=Listbox(ashu,exportselection=False)
    l1.pack(side=LEFT,padx=20)
    list1=["Consolas","Constantia","Albertus Extra Bold","Arial","Book Antiqua","Boulder","Calligrapher"
           ,"Arial Black","Chaucer","Comic Sans","Arrus BT","BinnerD","BREMEN BD BT","llucida"]
    for i in list1:
        l1.insert(END,i)

    l3=Listbox(ashu,exportselection=False)
    l3.pack(side=LEFT,padx=20)
    list2=["bold","normal","italic","bold italic"]
    for i in list2:
        l3.insert(END,i)

    l2=Listbox(ashu,exportselection=False)
    l2.pack(side=LEFT,padx=20)
    for i in range(10,100,2):
        l2.insert(END,i)
    l1.select_set(1)
    l2.select_set(9)
    l3.select_set(1)


def bag():
    import random
    p=("yellow","red","green","pink","blue","skyblue","gray","brown","orange")
    k=random.choice(p)
    t.configure(bg=k)

t=Text(root,font="llucida 30 bold")
t.pack(expand=True,fill=BOTH)

menubar=Menu(root)
menubar1=Menu(menubar,tearoff=0)
menubar1.add_command(label="New_File",command=newfile)
menubar1.add_command(label="Open_File",command=openfile)
menubar1.add_command(label="Save_File",command=savefile)
menubar1.add_separator()
menubar1.add_command(label="Exit",command=Quit)
menubar.add_cascade(label="Files",menu=menubar1)
root.config(menu=menubar)

menubar1=Menu(menubar,tearoff=0)
menubar1.add_command(label="Cut",command=cut)
menubar1.add_command(label="copy",command=Copy)
menubar1.add_command(label="paste",command=Paste)
menubar1.add_separator()
menubar.add_cascade(label="Edit",menu=menubar1)

menubar1=Menu(menubar,tearoff=0)
menubar1.add_command(label="Font",command=font)
menubar1.add_command(label="Background_colour",command=bag)
menubar1.add_separator()
menubar.add_cascade(label="Format",menu=menubar1)

menubar1=Menu(menubar)
menubar1.add_command(label="About",command=About)
root.config(menu=menubar)
menubar.add_cascade(label="More",menu=menubar1)
menubar1=Menu(menubar)

#adding a scrollbar
scrollBar=Scrollbar(t)
scrollBar.pack(side=RIGHT,fill=BOTH)
scrollBar.config(command=t.yview)
t.config(yscrollcommand=scrollBar.set)
root.mainloop()

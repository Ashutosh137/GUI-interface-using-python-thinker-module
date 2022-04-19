#Importing a tkinter module
from tkinter import *
from tkinter.messagebox import showerror,_show
from math import sin, cos, tan, asin, acos, atan,pi

#creating a window
root=Tk()
sc=StringVar()
sc.set("")

f0 = Frame(root, bg="Blue", pady=2)

def About():
    _show("calculator by Ashutosh Sharma","This calculetor is coded by ashutosh sharma "
                                       "this calculator is prepared by the help of tkinter module in python programming  "
                                       "Contact us:- gmail id  Mr.luckysharma7@gmail.com ")

def science():
    global f0
    for widgets in f0.winfo_children():
        widgets.destroy()

    def ex(number):
        o = ["sin", "cos", "tan", "sinax", "cosax", "tanax"]
        not_a_number = ["=", 'c', 'del', "%","1/x","log","ln","sin", "cos", "tan", "sinax", "cosax", "tanax"]
        if number not in not_a_number:
            screen.insert(END, number)
        elif number == '1/x':
            try:
                a=eval(sc.get())
                b=1/a
                sc.set(b)
            except:
                pass
        elif number == 'log':
            a = eval(sc.get())
            try:
                sc.set(math.log10(a))
            except:
                pass


        elif number == 'ln':
            a = eval(sc.get())
            try:
                sc.set(math.log(a,2.3))
            except:
                pass
        elif number == "c":
            sc.set(" ")
        elif number == "%":
            try:
                b = int(sc.get())
                a = b / 100
                sc.set(a)
            except:
                pass

        elif number == "del":
            screen.delete(len(sc.get()) - 1, END)
        elif number == "e":
            screen.insert(END, number)

        try:
            if number=="sin":
                a = pi * eval(sc.get()) / 180
                b = sin(a)
                sc.set(b)
            if number=="cos":
                a = pi * eval(sc.get()) / 180
                b = cos(a)
                sc.set(b)
            if number=="tan":
                a = pi * eval(sc.get()) / 180
                b = tan(a)
                sc.set(b)
            if number=="sinax":
                a = pi * eval(sc.get()) / 180
                b = asin(a)
                sc.set(b)
            elif number=="cosax":
                a = pi * eval(sc.get()) / 180
                b = acos(a)
                sc.set(b)
            elif number=="tanax":
                a = pi * eval(sc.get()) / 180
                b = atan(a)
                sc.set(b)
            elif number == '=':
                e=2.3
                a = eval(sc.get())
                sc.set(a)
        except:
            pass
    #creating a screen
    screen = Entry(f0, textvar=sc, font="llucida 30 bold")
    screen.grid(row=0, columnspan=7, column=0, pady=12,ipadx=100)
    colour="white"

    #creating Buttons
    Button(f0, text=".", font="llucida 30 bold", command=lambda: ex('.'), activebackground="gray",
           background=colour).grid(ipadx=36.4, row=5, column=0)
    Button(f0, text=0, font="llucida 30 bold", command=lambda: ex(0), activebackground="gray",
           background=colour).grid(ipadx=31, row=5, column=1)
    Button(f0, text="e", font="llucida 30 bold", command=lambda: ex("e"), activebackground="gray",
           background=colour).grid(ipadx=32.5, row=5, column=2)
    Button(f0, text="=", font="llucida 30 bold", command=lambda: ex('='), activebackground="gray",
           background=colour).grid(ipadx=30, row=5, column=3)

    Button(f0, text=1, font="llucida 30 bold", command=lambda: ex(1), activebackground="gray",
           background=colour).grid(ipadx=31, row=4, column=0)
    Button(f0, text=2, font="llucida 30 bold", command=lambda: ex(2), activebackground="gray",
           background=colour).grid(ipadx=31, row=4, column=1)
    Button(f0, text=3, font="llucida 30 bold", command=lambda: ex(3), activebackground="gray",
           background=colour).grid(ipadx=33, row=4, column=2)
    Button(f0, text="+", font="llucida 30 bold", command=lambda: ex("+"), activebackground="gray",
           background=colour).grid(ipadx=30, row=4, column=3)

    Button(f0, text=4, font="llucida 30 bold", command=lambda: ex(4), activebackground="gray",
           background=colour).grid(ipadx=31, row=3, column=0)
    Button(f0, text=5, font="llucida 30 bold", command=lambda: ex(5), activebackground="gray",
           background=colour).grid(ipadx=31, row=3, column=1)
    Button(f0, text=6, font="llucida 30 bold", command=lambda: ex(6), activebackground="gray",
           background=colour).grid(ipadx=33, row=3, column=2)
    Button(f0, text="-", font="llucida 30 bold", command=lambda: ex('-'), activebackground="gray",
           background=colour).grid(ipadx=35, row=3, column=3)

    Button(f0, text=7, font="llucida 30 bold", command=lambda: ex(7), activebackground="gray",
           background=colour).grid(ipadx=31, row=2, column=0)
    Button(f0, text=8, font="llucida 30 bold", command=lambda: ex(8), activebackground="gray",
           background=colour).grid(ipadx=31, row=2, column=1)
    Button(f0, text=9, font="llucida 30 bold", command=lambda: ex(9), activebackground="gray",
           background=colour).grid(ipadx=33, row=2, column=2)
    Button(f0, text="x", font="llucida 30 bold", command=lambda: ex('*'), activebackground="gray",
           background=colour).grid(ipadx=31, row=2, column=3)

    Button(f0, text="C", font="llucida 30 bold", command=lambda: ex('c'), activebackground="gray",
           background="chartreuse").grid(ipadx=27.4, row=1, column=0)
    Button(f0, text='%', font="llucida 30 bold", command=lambda: ex('%'), activebackground="gray",
           background=colour).grid(ipadx=25, row=1, column=1)
    Button(f0, text='Del', font="llucida 30 bold", command=lambda: ex("del"), activebackground="gray",
           background=colour).grid(ipadx=13, row=1, column=2)
    Button(f0, text="/", font="llucida 30 bold", command=lambda: ex('/'), activebackground="gray",
           background=colour).grid(ipadx=36, row=1, column=3)

    Button(f0, text="sin", font="llucida 30 bold", command=lambda: ex('sin'), activebackground="gray",
           background=colour).grid(ipadx=17, row=5, column=5)
    Button(f0, text='cos', font="llucida 30 bold", command=lambda: ex('cos'), activebackground="gray",
           background=colour).grid(ipadx=11, row=4, column=5)
    Button(f0, text='tan', font="llucida 30 bold", command=lambda: ex("tan"), activebackground="gray",
           background=colour).grid(ipadx=16, row=3, column=5)
    Button(f0, text="1/x", font="llucida 30 bold", command=lambda: ex('1/x'), activebackground="gray",
           background=colour).grid(ipadx=18, row=2, column=5)
    Button(f0, text="log ", font="llucida 30 bold", command=lambda: ex('log'), activebackground="gray",
           background=colour).grid(ipadx=10, row=1, column=5)

    Button(f0, text="sinax", font="llucida 30 bold", command=lambda: ex('sinax'), activebackground="gray",
           background=colour).grid(ipadx=6, row=5, column=6)
    Button(f0, text='cosax', font="llucida 30 bold", command=lambda: ex('cosax'), activebackground="gray",
           background=colour).grid(ipadx=0, row=4, column=6)
    Button(f0, text='tanax', font="llucida 30 bold", command=lambda: ex("tanax"), activebackground="gray",
           background=colour).grid(ipadx=5, row=3, column=6)
    Button(f0, text="^", font="llucida 30 bold", command=lambda: ex('**'), activebackground="gray",
           background=colour).grid(ipadx=44, row=2, column=6)
    Button(f0, text="ln", font="llucida 30 bold", command=lambda: ex('ln'), activebackground="gray",
           background=colour).grid(ipadx=39, row=1, column=6)


    f0.grid(row=0, column=0)

    # Adding a menubar
    menubar = Menu(root)
    menubar1 = Menu(menubar, tearoff=0)
    menubar1.add_command(label="Normal Calculator", command=normal)
    menubar1.add_command(label="Exit", command=quit)
    menubar.add_cascade(label="Switch Calculator", menu=menubar1)
    root.config(menu=menubar)

    menubar1 = Menu(menubar,tearoff=0)
    menubar1.add_command(label="About", command=About)
    root.config(menu=menubar)
    menubar.add_cascade(label="More", menu=menubar1)
    menubar1 = Menu(menubar)


def normal():

    global  f0
    for widgets in f0.winfo_children():
        widgets.destroy()

    f0 = Frame(root, bg="blue", pady=2)

    screen = Entry(f0, textvar=sc, font="llucida 30 bold")
    screen.grid(row=0, columnspan=6, column=0, pady=12)
    f0.grid(row=0, column=0)
    def ex(number):
        not_a_number = ["=", 'c', 'del', "%"]
        if number not in not_a_number:
            screen.insert(END, number)

        elif number == '=':

            try:
                a = eval(sc.get())
                sc.set(a)
            except:
                 showerror("Syntex Error","Invalid Syntex")
        elif number == "c":
            sc.set(" ")
        elif number == "%":
            try:
                b = int(sc.get())
                a = b / 100
                sc.set(a)
            except:
                pass
        elif number == "del":
            screen.delete(len(sc.get()) - 1, END)

    f0 = Frame(root, bg="blue", pady=2)

    screen = Entry(f0, textvar=sc, font="llucida 30 bold")
    screen.grid(row=0, columnspan=6, column=0, pady=12)


    Button(f0, text=".", font="llucida 30 bold", command=lambda: ex('.'), activebackground="gray",
           background="yellow").grid(ipadx=36.5, row=5, column=0)
    Button(f0, text=0, font="llucida 30 bold", command=lambda: ex(0), activebackground="gray",
           background="yellow").grid(ipadx=31, row=5, column=1)
    Button(f0, text="00", font="llucida 30 bold", command=lambda: ex("00"), activebackground="gray",
           background="yellow").grid(ipadx=22, row=5, column=2)
    Button(f0, text="=", font="llucida 30 bold", command=lambda: ex('='), activebackground="gray",

           background="yellow").grid(ipadx=30, row=5, column=3)

    Button(f0, text=1, font="llucida 30 bold", command=lambda: ex(1), activebackground="gray",
           background="yellow").grid(ipadx=31.5, row=4, column=0)
    Button(f0, text=2, font="llucida 30 bold", command=lambda: ex(2), activebackground="gray",
           background="yellow").grid(ipadx=31, row=4, column=1)
    Button(f0, text=3, font="llucida 30 bold", command=lambda: ex(3), activebackground="gray",
           background="yellow").grid(ipadx=33, row=4, column=2)
    Button(f0, text="+", font="llucida 30 bold", command=lambda: ex("+"), activebackground="gray",
           background="yellow").grid(ipadx=30, row=4, column=3)

    Button(f0, text=4, font="llucida 30 bold", command=lambda: ex(4), activebackground="gray",
           background="yellow").grid(ipadx=31.5, row=3, column=0)
    Button(f0, text=5, font="llucida 30 bold", command=lambda: ex(5), activebackground="gray",
           background="yellow").grid(ipadx=31, row=3, column=1)
    Button(f0, text=6, font="llucida 30 bold", command=lambda: ex(6), activebackground="gray",
           background="yellow").grid(ipadx=33, row=3, column=2)
    Button(f0, text="-", font="llucida 30 bold", command=lambda: ex('-'), activebackground="gray",
           background="yellow").grid(ipadx=35, row=3, column=3)

    Button(f0, text=7, font="llucida 30 bold", command=lambda: ex(7), activebackground="gray",
           background="yellow").grid(ipadx=31.5, row=2, column=0)
    Button(f0, text=8, font="llucida 30 bold", command=lambda: ex(8), activebackground="gray",
           background="yellow").grid(ipadx=31, row=2, column=1)
    Button(f0, text=9, font="llucida 30 bold", command=lambda: ex(9), activebackground="gray",
           background="yellow").grid(ipadx=33, row=2, column=2)
    Button(f0, text="x", font="llucida 30 bold", command=lambda: ex('*'), activebackground="gray",
           background="yellow").grid(ipadx=31, row=2, column=3)

    Button(f0, text="C", font="llucida 30 bold", command=lambda: ex('c'), activebackground="gray",
           background="chartreuse").grid(ipadx=27.5, row=1, column=0)
    Button(f0, text='%', font="llucida 30 bold", command=lambda: ex('%'), activebackground="gray",
           background="yellow").grid(ipadx=25, row=1, column=1)
    Button(f0, text='Del', font="llucida 30 bold", command=lambda: ex("del"), activebackground="gray",
           background="yellow").grid(ipadx=13, row=1, column=2)
    Button(f0, text="/", font="llucida 30 bold", command=lambda: ex('/'), activebackground="gray",
           background="yellow").grid(ipadx=35.5, row=1, column=3)

    f0.grid(row=0, column=0)

    # Adding a menubar
    menubar = Menu(root)
    menubar1 = Menu(menubar, tearoff=0)
    menubar1.add_command(label="Scientific Calculator", command=science)
    menubar1.add_command(label="Exit", command=quit)
    menubar.add_cascade(label="Switch Calculator", menu=menubar1)

    menubar1 = Menu(menubar,tearoff=0)
    menubar1.add_command(label="About", command=About)
    root.config(menu=menubar)
    menubar.add_cascade(label="More", menu=menubar1)
    root.config(menu=menubar)

normal()
root.mainloop()

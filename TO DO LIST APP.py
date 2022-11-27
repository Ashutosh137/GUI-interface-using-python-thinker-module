from tkinter import *
from tkinter.messagebox import showerror,_show
from time import strftime
root=Tk()
x,y=1,1
task_list=[]
root.title("TO-DO-LIST")
root.geometry("400x650")
color="navy"
root.config(background=color)
logo=PhotoImage(file="tech/topbar.png")
plus=PhotoImage(file="tech/plus.png")
frame=Frame(root,bg=color)
Label(root,image=logo).pack()
delete=PhotoImage(file="tech/delete.png")
import datetime
def ex():
    pass

def f():
    def cancel():
        root1.destroy()

    def ok():
        global x,y

        if x==1:

            Label(frame,text="Your Tasks",font="llucida 10 bold",padx=10,pady=10).grid(row=1,column=0)
            Label(frame,text="Till",font="llucida 10 bold",padx=10,pady=10).grid(row=1,column=1)


        if sc.get()!="":
            x+=1
            y=0
            Checkbutton(frame,text=sc.get(),font="llucida 10 bold",padx=10,pady=10).grid(row=x,column=y,padx=10,pady=10)

        if datetime.datetime.now()>sc.get():
            y=1
            Label(frame,text=st.get(),colour="red",font="llucida 10 bold",padx=10,pady=10).grid(row=x,column=y,padx=10,pady=10)
            Button(frame,image=delete,width=30,height=30,command=ex()).grid(row=x,column=y+1,padx=10,pady=10)
        else:
            y=1
            Label(frame,text=st.get(),colour="blue",font="llucida 10 bold",padx=10,pady=10).grid(row=x,column=y,padx=10,pady=10)
            Button(frame,image=delete,width=30,height=30,command=ex()).grid(row=x,column=y+1,padx=10,pady=10)
        root1.destroy()

    sc=StringVar()
    st=StringVar()
    sc.set("")
    
    root1=Toplevel(root)
    root1.config(background=color)
    time_string=strftime('%a, %d %b %Y %H:%M')
    st.set(time_string)
    Label(root1,bg=color,fg="white",text="Enter Your Task",font="llucida 10 bold").grid(row=0,column=0,padx=10,pady=10)
    screen = Entry(root1, textvar=sc, font="llucida 10 bold").grid(row=1,column=0,padx=10,pady=10)
    Label(root1,text="Date",fg="white",bg=color,font="llucida 10 bold").grid(row=2,column=0,padx=10,pady=10)
    screen = Entry(root1, textvar=st, font="llucida 10 bold").grid(row=3,column=0,padx=10,pady=10)
    Button(root1,text="OK",command=ok).grid(row=4,column=0)
    Button(root1,text="cancel",command=cancel).grid(row=5,column=0)
frame.pack()
Button(root,image=plus,font="llucida 10 bold",command=f,width=40,height=40,padx=20).pack(side=BOTTOM,padx=20,pady=20)
root.mainloop()
from tkinter import *
import csv
import time
import random
import datetime
import tkinter.ttk as ttk
l1=[]
l2=[]
l3=[]
n=0
x=0
y=0
def L():
    i1=Tk()
    i1.geometry("1000x560+150+90")
    i1.minsize("1000","560")
    i1.maxsize("1000","560")

    bg = PhotoImage(file=r"photos\background.png")



    label2=Label(i1,image=bg)
    label2.place(x=0,y=0)


    label1=Label(i1,text="Planetary Pairs",font="times 25 italic ",background="white")
    label1.pack(side="top",ipadx=50,ipady=20,pady=100)

    
    def click():
        global x
        if x==0:
            i1.destroy()
        x=x+1
        global l3
        l3=[]
        i2=Tk()
            
        name=Label(i2,text="Enter your name",font="times 15")
        name.pack(side="top")

        Name=StringVar(i2)
        e1=Entry(i2,textvariable=Name)
        e1.pack(side="top")
        def z():
            i2.destroy()
        submit=Button(i2,text="submit",command=z)
        submit.pack(side="top")
            
        i2.mainloop()
        
        if Name.get():
            t1=time.time()
            i3=Tk()
            i3.configure(cursor="shuttle")

            l=["Mercury","Venus","Earth","Mars","jupiter","Saturn","Uranus","Neptune"]*2
            random.shuffle(l)

            b1=Button(i3,text="1")
            b2=Button(i3,text="1")
            b3=Button(i3,text="1")
            b4=Button(i3,text="1")
            b5=Button(i3,text="1")
            b6=Button(i3,text="1")
            b7=Button(i3,text="1")
            b8=Button(i3,text="1")
            b9=Button(i3,text="1")
            b10=Button(i3,text="1")
            b11=Button(i3,text="1")
            b12=Button(i3,text="1")
            b13=Button(i3,text="1")
            b14=Button(i3,text="1")
            b15=Button(i3,text="1")
            b16=Button(i3,text="1")

            class button_command:
                def __init__(self,button,text):
                    self.text=text
                    self.button=button
                def f(self):
                    global l1
                    global l2
                    global l3
                    global n
                    global x
                    if self.button not in l2:
                        l1.append(self.text)
                        l2.append(self.button)
                        self.button.configure(text=self.text)
                        if len(l2)!=0:
                            if len(l1)==2:
                                self.button.update_idletasks()
                                time.sleep(0.8)
                                if l1[0]!=l1[1]:
                                    for i in l2:
                                        i.configure(text="1")
                                    l1=[]
                                    l2=[]
                                    n=n+1
                                else:
                                    for i in l2:
                                        if x>1:
                                            i.configure(command=lambda:None)
                                        l3.append(i)
                                    l1=[]
                                    l2=[]
                                    n=n+1
                    if len(l3)==16:
                        t2=time.time()
                        i3.destroy()
                        i4=Tk()
                        p1=Label(i4,text="Congratulation!!\n You Won",font="times 25 italic")
                        p1.pack(side="top")
                        p2=Label(i4,text=f"score\n Number of moves taken : {n}\n Time taken : {str(datetime.timedelta(seconds=t2-t1))[2:7]}",font="times 15")
                        p2.pack(side="top",fill="x")
                        def P():
                            i4.destroy()
                            click()
                        c1=Button(i4,text="Replay",font="times 20",command=P)
                        c1.pack(side="left",expand=True,fill=X,padx=100,ipadx=20,ipady=10)
                        def R():
                            i4.destroy()
                            L()
                        c2=Button(i4,text="Home",font="times 20",command=R)
                        c2.pack(side="right",expand=TRUE,fill=X,padx=80,ipadx=20,ipady=10)

            a=button_command(b1,l[0])
            b=button_command(b2,l[1])
            c=button_command(b3,l[2])
            d=button_command(b4,l[3])
            e=button_command(b5,l[4])
            f=button_command(b6,l[5])
            g=button_command(b7,l[6])
            h=button_command(b8,l[7])
            i=button_command(b9,l[8])
            j=button_command(b10,l[9])
            k=button_command(b11,l[10])
            Q=button_command(b12,l[11])
            m=button_command(b13,l[12])
            n=button_command(b14,l[13])
            o=button_command(b15,l[14])
            p=button_command(b16,l[15])

            b1.configure(command=a.f)
            b2.configure(command=b.f)
            b3.configure(command=c.f)
            b4.configure(command=d.f)
            b5.configure(command=e.f)
            b6.configure(command=f.f)
            b7.configure(command=g.f)
            b8.configure(command=h.f)
            b9.configure(command=i.f)
            b10.configure(command=j.f)
            b11.configure(command=k.f)
            b12.configure(command=Q.f)
            b13.configure(command=m.f)
            b14.configure(command=n.f)
            b15.configure(command=o.f)
            b16.configure(command=p.f)

            i3.rowconfigure(0,weight=1)
            i3.rowconfigure(1,weight=1)
            i3.rowconfigure(2,weight=1)
            i3.rowconfigure(3,weight=1)
            i3.columnconfigure(0,weight=1)
            i3.columnconfigure(1,weight=1)
            i3.columnconfigure(2,weight=1)
            i3.columnconfigure(3,weight=1)

            b1.grid(row=0,column=0,sticky=NSEW)

            b2.grid(row=0,column=1,sticky=NSEW)

            b3.grid(row=0,column=2,sticky=NSEW)

            b4.grid(row=0,column=3,sticky=NSEW)

            b5.grid(row=1,column=0,sticky=NSEW)

            b6.grid(row=1,column=1,sticky=NSEW)

            b7.grid(row=1,column=2,sticky=NSEW)

            b8.grid(row=1,column=3,sticky=NSEW)

            b9.grid(row=2,column=0,sticky=NSEW)

            b10.grid(row=2,column=1,sticky=NSEW)

            b11.grid(row=2,column=2,sticky=NSEW)

            b12.grid(row=2,column=3,sticky=NSEW)

            b13.grid(row=3,column=0,sticky=NSEW)

            b14.grid(row=3,column=1,sticky=NSEW)

            b15.grid(row=3,column=2,sticky=NSEW)

            b16.grid(row=3,column=3,sticky=NSEW)

            i3.mainloop()
    def read():
        i5=Tk()
        s1=Label(i5,text="Scores",font="times 40")
        s1.pack(side="top")
        f1=Frame(i5,height=0,background="red")
        f1.pack(side="top")
        columns = ("Name","No.of Moves","Time Taken")

        tree = ttk.Treeview(f1, columns=columns, show="headings",height=13)

        tree.heading("Name", text="Name")
        tree.heading("No.of Moves", text="No.of Moves")
        tree.heading("Time Taken", text="Time Taken")

        with open(r"keyur\record.csv","r") as B:
            csv_reader =csv.reader(B)

            for i in csv_reader:
                if len(i)!=0:
                    tree.insert("",END, values=i)

        tree.pack(side="left",ipadx=180)

        scrollbar = ttk.Scrollbar(f1, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="left",fill="y")

        s2=Label(i5,text="High Score",font="times 40")
        s2.pack(side="top")
        M=[]
        T=[]
        with open(r"keyur\record.csv","r") as B:
            csv_reader =csv.reader(B)
            for i in csv_reader:
                M.append(i[1])
                T.append(i[2])

            s3=Label(i5,text=f"Least No.of Moves Achived : {min(M)}\n Least Time Taken : {min(T)}",font="times 25")
            s3.pack()
        i5.mainloop()

    button1=Button(i1,text="New Game",font="times 15 bold",background="white",command=click)
    button1.pack(side="left",expand=True,fill=X,padx=100,ipadx=20,ipady=10)

    button2=Button(i1,text="View History",font="times 15 bold",background="white",command=read)
    button2.pack(side="right",expand=TRUE,fill=X,padx=80,ipadx=20,ipady=10)

    i1.mainloop()
L()
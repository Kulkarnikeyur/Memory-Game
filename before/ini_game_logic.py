from tkinter import *
import random
import time
i2=Tk()
l=["Mercury","Venus","Mercury","Venus"]

random.shuffle(l)

l1=[]
l2=[]
l3=[]

b1=Button(i2,text="1")
b2=Button(i2,text="1")
b3=Button(i2,text="1")
b4=Button(i2,text="1")

class button_command:
    def __init__(self,button,text):
        self.text=text
        self.button=button
    def f(self):
        global l1
        global l2
        global l3
        if self.button not in l2:
            l1.append(self.text)
            l2.append(self.button)
            self.button.configure(text=self.text)
            if len(l2)!=0:
                if len(l1)==2:
                    self.button.update_idletasks()
                    time.sleep(2)
                    if l1[0]!=l1[1]:
                        for i in l2:
                            i.configure(text="1")
                        l1=[]
                        l2=[]
                    else:
                        for i in l2:
                            i.configure(command=lambda:None)
                            l3.append(i)
                        l1=[]
                        l2=[]
        # print(l1)
        # print(l2)
        if len(l3)==4:
            i2.destroy()
            i3=Tk()
            p1=Label(i3,text="Congratulation!!\n You won",font="times 25 italic")
            i3.rowconfigure(0,weight=1)
            i3.columnconfigure(0,weight=1)
            p1.grid(row=0,column=0,sticky=NSEW)


w=button_command(b1,l[0])
x=button_command(b2,l[1])
y=button_command(b3,l[2])
z=button_command(b4,l[3])

b1.configure(command=w.f)
b2.configure(command=x.f)
b3.configure(command=y.f)
b4.configure(command=z.f)



i2.rowconfigure(0,weight=1)
i2.rowconfigure(1,weight=1)
i2.columnconfigure(0,weight=1)
i2.columnconfigure(1,weight=1)

b1.grid(row=0,column=0,sticky=NSEW)

b2.grid(row=0,column=1,sticky=NSEW)

b3.grid(row=1,column=0,sticky=NSEW)

b4.grid(row=1,column=1,sticky=NSEW)


i2.mainloop()
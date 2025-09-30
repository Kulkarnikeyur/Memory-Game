from tkinter import *
import csv
import time
import random
import datetime
import tkinter.ttk as ttk
from tkinter import messagebox
import pygame

l1 = []
l2 = []
l3 = []
Gname = ""  # store name here
n = 0


def L():
    i1 = Tk()
    i1.title("Memory Game")
    i1.geometry("1000x560+150+90")
    i1.minsize("1000", "560")
    i1.maxsize("1000", "560")

    bg = PhotoImage(file=r"Memory-Game\photos\main_background.png")

    label2 = Label(i1, image=bg)
    label2.place(x=0, y=0)

    label1 = Label(
        i1, text="Planetary Pairs", font="times 25 italic ", background="white"
    )
    label1.pack(side="top", ipadx=50, ipady=20, pady=100)

    def click():
        global n, l3, Gname
        n = 0
        l3 = []
        try:
            i1.destroy()
        except:
            pass

        # ---- CHANGED HERE ----
        if not Gname:  # ask name only if not set yet
            i2 = Tk()
            i2.geometry("150x130+550+250")
            i2.minsize("150", "130")
            i2.maxsize("150", "130")

            name = Label(i2, text="Enter your name", font="times 15")
            name.pack(side="top")

            Name = StringVar(i2)
            e1 = Entry(i2, textvariable=Name)
            e1.pack(side="top", pady=5)

            def z():
                global Gname
                if Name.get():
                    Gname = Name.get()  # save permanently
                    i2.destroy()
                    pygame.mixer.init()
                    pygame.mixer.music.load(r"Memory-Game\sounds\game-start-6104.mp3")
                    pygame.mixer.music.play(loops=0)
                else:
                    messagebox.showinfo(title="Error", message="Please enter your name")

            submit = Button(i2, text="submit", command=z)
            submit.pack(side="top")

            def Back():
                i2.destroy()
                L()

            backk = Button(i2, text="Back", command=Back)
            backk.pack(side="top", pady=5)

            i2.mainloop()
        else:
            # if already have name, just play sound and continue
            pygame.mixer.init()
            pygame.mixer.music.load(r"Memory-Game\sounds\game-start-6104.mp3")
            pygame.mixer.music.play(loops=0)
        # ---- END CHANGE ----

        t1 = time.time()
        i3 = Tk()
        i3.geometry("668x668+350+1")
        i3.minsize("668", "668")
        i3.maxsize("668", "668")
        i3.configure(cursor="shuttle")
        backbutton = PhotoImage(file=r"Memory-Game\photos\background.png")
        mercury = PhotoImage(file=r"Memory-Game\photos\mercury.png")
        venus = PhotoImage(file=r"Memory-Game\photos\venus.png")
        earth = PhotoImage(file=r"Memory-Game\photos\earth.png")
        mars = PhotoImage(file=r"Memory-Game\photos\mars.png")
        jupiter = PhotoImage(file=r"Memory-Game\photos\jupiter.png")
        saturn = PhotoImage(file=r"Memory-Game\photos\saturn.png")
        uranus = PhotoImage(file=r"Memory-Game\photos\uranus.png")
        neptune = PhotoImage(file=r"Memory-Game\photos\neptune.png")

        l = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune] * 2
        random.shuffle(l)
        b1 = Button(i3, image=backbutton)
        b2 = Button(i3, image=backbutton)
        b3 = Button(i3, image=backbutton)
        b4 = Button(i3, image=backbutton)
        b5 = Button(i3, image=backbutton)
        b6 = Button(i3, image=backbutton)
        b7 = Button(i3, image=backbutton)
        b8 = Button(i3, image=backbutton)
        b9 = Button(i3, image=backbutton)
        b10 = Button(i3, image=backbutton)
        b11 = Button(i3, image=backbutton)
        b12 = Button(i3, image=backbutton)
        b13 = Button(i3, image=backbutton)
        b14 = Button(i3, image=backbutton)
        b15 = Button(i3, image=backbutton)
        b16 = Button(i3, image=backbutton)

        class Memory_Game:
            def __init__(self, button, text):
                self.text = text
                self.button = button

            def f(self):
                global l1
                global l2
                global l3
                global n
                global Gname
                if self.button not in l2:
                    l1.append(self.text)
                    l2.append(self.button)
                    self.button.configure(image=self.text)
                    if len(l2) != 0:
                        if len(l1) == 2:
                            self.button.update_idletasks()
                            time.sleep(0.4)
                            if l1[0] != l1[1]:
                                for i in l2:
                                    i.configure(image=backbutton)
                                l1 = []
                                l2 = []
                                n = n + 1
                            else:
                                for i in l2:
                                    pygame.mixer.init()
                                    pygame.mixer.music.load(
                                        r"Memory-Game\sounds\correct response.mp3"
                                    )
                                    pygame.mixer.music.play(loops=0)
                                    i.configure(command=lambda: None)
                                    l3.append(i)
                                l1 = []
                                l2 = []
                                n = n + 1
                if len(l3) == 16:
                    t2 = time.time()
                    with open(r"Memory-Game\record.csv", "r") as A:
                        csv_reader = csv.reader(A)
                        next(csv_reader)
                        K = 1
                        for i in csv_reader:
                            K += 1
                    with open(r"Memory-Game\record.csv", "a") as A:
                        A.write(
                            f"{K},{Gname},{n},{str(datetime.timedelta(seconds=t2-t1))[2:7]}\n"
                        )
                    with open(r"Memory-Game\record.csv", "r") as A:
                        csv_reader = csv.reader(A)
                        next(csv_reader)
                    i3.destroy()
                    i4 = Tk()
                    i4.geometry("630x350+400+150")
                    i4.minsize("630", "350")
                    i4.maxsize("630", "350")
                    p1 = Label(
                        i4,
                        text=f"Congratulations {Gname}!!\n You cracked it",
                        font="times 25 italic",
                    )
                    p1.pack(side="top")
                    p2 = Label(
                        i4,
                        text=f"score\n Number of moves taken : {n}\n Time taken : {str(datetime.timedelta(seconds=t2-t1))[2:7]}",
                        font="times 20",
                    )
                    p2.pack(side="top", fill="x")

                    def P():
                        i4.destroy()
                        click()

                    M = []
                    T = []
                    with open(r"Memory-Game\record.csv", "r") as B:
                        csv_reader = csv.reader(B)
                        next(csv_reader)
                        for i in csv_reader:
                            M.append(int(i[2]))
                            T.append(i[3])
                    if len(M) > 1:
                        if min(M) == n:
                            p3 = Label(
                                i4,
                                text=f"{Gname}!! You did it in least number of moves",
                                font="times 20 italic",
                            )
                            p3.pack(side="top")
                        if min(T) == str(datetime.timedelta(seconds=t2 - t1))[2:7]:
                            p4 = Label(
                                i4,
                                text=f"{Gname}!! You did it in least time",
                                font="times 20 italic",
                            )
                            p4.pack(side="top")
                    c1 = Button(i4, text="Replay", font="times 20", command=P)
                    c1.pack(
                        side="left", expand=True, fill=X, padx=60, ipadx=10, ipady=5
                    )

                    def R():
                        i4.destroy()
                        L()

                    c2 = Button(i4, text="Home", font="times 20", command=R)
                    c2.pack(
                        side="right", expand=TRUE, fill=X, padx=40, ipadx=10, ipady=5
                    )

        a = Memory_Game(b1, l[0])
        b = Memory_Game(b2, l[1])
        c = Memory_Game(b3, l[2])
        d = Memory_Game(b4, l[3])
        e = Memory_Game(b5, l[4])
        f = Memory_Game(b6, l[5])
        g = Memory_Game(b7, l[6])
        h = Memory_Game(b8, l[7])
        i = Memory_Game(b9, l[8])
        j = Memory_Game(b10, l[9])
        k = Memory_Game(b11, l[10])
        Q = Memory_Game(b12, l[11])
        m = Memory_Game(b13, l[12])
        N = Memory_Game(b14, l[13])
        o = Memory_Game(b15, l[14])
        p = Memory_Game(b16, l[15])

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
        b14.configure(command=N.f)
        b15.configure(command=o.f)
        b16.configure(command=p.f)

        i3.rowconfigure(0, weight=1)
        i3.rowconfigure(1, weight=1)
        i3.rowconfigure(2, weight=1)
        i3.rowconfigure(3, weight=1)
        i3.columnconfigure(0, weight=1)
        i3.columnconfigure(1, weight=1)
        i3.columnconfigure(2, weight=1)
        i3.columnconfigure(3, weight=1)

        b1.grid(row=0, column=0, sticky=NSEW)
        b2.grid(row=0, column=1, sticky=NSEW)
        b3.grid(row=0, column=2, sticky=NSEW)
        b4.grid(row=0, column=3, sticky=NSEW)
        b5.grid(row=1, column=0, sticky=NSEW)
        b6.grid(row=1, column=1, sticky=NSEW)
        b7.grid(row=1, column=2, sticky=NSEW)
        b8.grid(row=1, column=3, sticky=NSEW)
        b9.grid(row=2, column=0, sticky=NSEW)
        b10.grid(row=2, column=1, sticky=NSEW)
        b11.grid(row=2, column=2, sticky=NSEW)
        b12.grid(row=2, column=3, sticky=NSEW)
        b13.grid(row=3, column=0, sticky=NSEW)
        b14.grid(row=3, column=1, sticky=NSEW)
        b15.grid(row=3, column=2, sticky=NSEW)
        b16.grid(row=3, column=3, sticky=NSEW)

        i3.mainloop()

    def read():
        i5 = Tk()
        i5.geometry("1175x560+100+90")
        i5.minsize("1175", "560")
        i5.maxsize("1175", "560")
        s1 = Label(i5, text="Scores", font="times 35")
        s1.pack(side="top")
        f1 = Frame(i5, height=0)
        f1.pack(side="top")
        columns = ("S.No", "Name", "No.of Moves", "Time Taken")
        try:
            tree = ttk.Treeview(f1, columns=columns, show="headings", height=13)

            tree.heading("S.No", text="S.No")
            tree.heading("Name", text="Name")
            tree.heading("No.of Moves", text="No.of Moves")
            tree.heading("Time Taken", text="Time Taken")

            tree.configure()

            with open(r"Memory-Game\record.csv", "r") as B:
                csv_reader = csv.reader(B)
                next(csv_reader)
                for i in csv_reader:
                    if len(i) != 0:
                        tree.insert("", END, values=i)

            tree.pack(side="left", ipadx=180)

            scrollbar = ttk.Scrollbar(f1, orient=VERTICAL, command=tree.yview)
            tree.configure(yscroll=scrollbar.set)
            scrollbar.pack(side="left", fill="y")

            s2 = Label(i5, text="High Score", font="times 40")
            s2.pack(side="top")
            M = []
            T = []
            with open(r"Memory-Game\record.csv", "r") as B:
                csv_reader = csv.reader(B)
                next(csv_reader)
                for i in csv_reader:
                    M.append(int(i[2]))
                    T.append(i[3])
                s3 = Label(
                    i5,
                    text=f"Least No.of Moves Achived : {min(M)}\n Least Time Taken : {min(T)}",
                    font="times 25",
                )
                s3.pack()

                bb = Button(i5, text="Back", font="times 15", command=i5.destroy)
                bb.pack(pady=15)
        except:
            p5 = Label(i5, text=f"NO RECORDS FOUND", font="times 20")
            p5.pack(side="top")

            bb = Button(i5, text="Back", font="times 15", command=i5.destroy)
            bb.pack(pady=15)
        i5.mainloop()

    button1 = Button(
        i1, text="New Game", font="times 15 bold", background="white", command=click
    )
    button1.pack(side="left", expand=True, fill=X, padx=100, ipadx=20, ipady=10)

    button2 = Button(
        i1, text="View History", font="times 15 bold", background="white", command=read
    )
    button2.pack(side="right", expand=TRUE, fill=X, padx=80, ipadx=20, ipady=10)

    def gameexit():
        i1.destroy()

    button3 = Button(
        i1, text="exit", font="times 15 bold", background="white", command=gameexit
    )
    button3.pack(side="bottom", expand=True, fill=X, padx=100, ipadx=20, ipady=10)

    i1.mainloop()


L()

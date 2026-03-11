from tkinter import *
import tkinter.ttk as ttk
import csv

def open_history_screen():

    root = Tk()
    root.title("Game History")
    root.geometry("1175x560+100+90")
    root.minsize("1175", "560")
    root.maxsize("1175", "560")

    Label(root, text="Scores", font="times 35").pack(side="top")

    f1 = Frame(root, height=0)
    f1.pack(side="top")
    columns = ("S.No", "Name", "No.of Moves", "Time Taken")
    try:
        tree = ttk.Treeview(f1, columns=columns, show="headings", height=13)

        tree.heading("S.No", text="S.No")
        tree.heading("Name", text="Name")
        tree.heading("No.of Moves", text="No.of Moves")
        tree.heading("Time Taken", text="Time Taken")

        tree.configure()

        with open("data/record.csv", "r") as B:
            csv_reader = csv.reader(B)
            next(csv_reader)
            for i in csv_reader:
                if len(i) != 0:
                    tree.insert("", END, values=i)

        tree.pack(side="left", ipadx=180)

        scrollbar = ttk.Scrollbar(f1, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="left", fill="y")

        s2 = Label(root, text="High Score", font="times 40")
        s2.pack(side="top")
        M = []
        T = []
        with open("data/record.csv", "r") as B:
            csv_reader = csv.reader(B)
            next(csv_reader)
            for i in csv_reader:
                M.append(int(i[2]))
                T.append(i[3])
            s3 = Label(
                    root,
                    text=f"Least No.of Moves Achived : {min(M)}\n Least Time Taken : {min(T)}",
                    font="times 25",
                )
            s3.pack()

    except:
        p5 = Label(root, text=f"NO RECORDS FOUND", font="times 20")
        p5.pack(side="top")

    def back():
        root.destroy()
        from gui.dashboard import open_dashboard
        open_dashboard()

    Button(root, text="Back", font="times 15", command=back).pack(pady=15)

    root.mainloop()